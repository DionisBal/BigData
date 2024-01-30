import sys
import psutil
import time
import matplotlib.pyplot as plt


def memory_usage(pid):
    process = psutil.Process(pid)
    mem = process.memory_percent()
    return mem


def vms_usage(pid):
    process = psutil.Process(pid)
    ram_percentage = process.memory_percent(memtype='vms')
    return ram_percentage


def cpu_usage(pid):
    process = psutil.Process(pid)
    cpu_percent = process.cpu_percent(0.1)
    cpu_times = process.cpu_times()
    return cpu_percent


def get_port_pid(port):
    connections = psutil.net_connections('tcp')
    for con in connections:
        if con.raddr != tuple():
            if con.raddr.port == port:
                return con.pid
        if con.laddr != tuple():
            if con.laddr.port == port:
                return con.pid
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    arguments = sys.argv[1:]
    if (arguments[0] != "-ports" and arguments[0] != "-pid") or len(arguments) == 1:
        raise Exception("Please specify at least one port or pid number")
    cpu_matrix = []
    mem_matrix = []
    ram_matrix = []
    print(arguments)
    while True:
        max_rss = 0
        max_vms = 0
        max_cpu = 0
        for p in range(len(arguments[1:])):
            if arguments[0] == '-ports':
                port = arguments[p + 1]
                pid = get_port_pid(int(port))
            else:
                pid = int(arguments[p+1])
            # pid = int(port)
            try:
                if cpu_usage(pid) / psutil.cpu_count() > max_cpu:
                    max_cpu = cpu_usage(pid) / psutil.cpu_count()

                if memory_usage(pid) > max_rss:
                    max_rss = memory_usage(pid)
                # print(memory_usage(pid))

                if vms_usage(pid) > max_vms:
                    max_vms = vms_usage(pid)
                # print(ram_usage(pid))

            except Exception:
                x = []
                y = []

                for tup in mem_matrix:
                    y.append(tup[0])
                    x.append(tup[1])

                plt.plot(x, y)
                plt.title("% RSS Usage")
                plt.show()

                x = []
                y = []

                for tup in cpu_matrix:
                    y.append(tup[0])
                    x.append(tup[1])

                plt.plot(x, y)
                plt.title("% CPU Usage")
                plt.show()

                x = []
                y = []
                for tup in ram_matrix:
                    y.append(tup[0])
                    x.append(tup[1])

                plt.plot(x, y)
                plt.title("% VMS Usage")

                plt.show()
                # plt.savefig(r'C:\Users\mdbal\Desktop\Bid_Data_Plots\ray_loop_4.png')
                exit(0)
        cpu_matrix.append((max_cpu, time.time()-start_time))
        mem_matrix.append((max_rss, time.time() - start_time))
        ram_matrix.append((max_vms, time.time() - start_time))
        time.sleep(0.1)
