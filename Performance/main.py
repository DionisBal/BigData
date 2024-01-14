import psutil
import os
import time


def memory_usage(pid):
    process = psutil.Process(pid)
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem


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
    while True:
        if psutil.pid_exists(get_port_pid(52593)):
            print(cpu_usage(get_port_pid(52593)))
            time.sleep(0.1)
        else:
            break

