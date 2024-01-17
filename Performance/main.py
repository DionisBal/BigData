import sys
import psutil
import time


def memory_usage(pid):
    process = psutil.Process(pid)
    mem = process.memory_percent()
    return mem


def ram_usage(pid):
    process = psutil.Process(pid)
    ram_percentage = process.memory_info()[1] / float(2 ** 20)
    ram_percentage = ram_percentage / psutil.virtual_memory().total
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
    if arguments[0] != "-ports" or len(arguments) == 1:
        raise Exception("Please specify at least one port number")
    cpu_matrix = [[]] * (len(arguments) - 1)
    mem_matrix = [[]] * (len(arguments) - 1)
    ram_matrix = [[]] * (len(arguments) - 1)
    while True:
        for p in range(len(arguments[1:])):
            port = arguments[p + 1]
            # pid = get_port_pid(int(port))
            pid = int(port)
            if psutil.pid_exists(pid):
                if cpu_usage(pid) > 0.01:
                    cpu_matrix[p].append((cpu_usage(pid), time.time() - start_time))
                    print(cpu_usage(pid))
                if memory_usage(pid) > 0.0001:
                    mem_matrix[p].append((memory_usage(pid), time.time() - start_time))
                    print(memory_usage(pid))

                ram_matrix[p].append((ram_usage(pid), time.time() - start_time))
                print(ram_usage(pid))
            else:
                print(cpu_matrix)
                exit(0)
        time.sleep(0.1)
