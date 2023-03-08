import psutil
import sys
from psutil import process_iter
from signal import SIGTERM # or SIGKILL
import asyncio
import time

from check_project_run import check_run


def get_pid(port):
    connections = psutil.net_connections()

    for con in connections:
        if con.raddr != tuple():
            if con.raddr.port == port:
                return con.pid, con.status
        if con.laddr != tuple():
            if con.laddr.port == port:
                return con.pid, con.status
    return -1

def terminate_port_process(port):
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == port:
                proc.send_signal(SIGTERM) # or SIGKILL

if __name__ == '__main__':
    
    # if len(sys.argv) > 1:
    #     pid = get_pid()
    #     if pid == -1:
    #         print(":: Not Found :<")
    #     else:
    #         print(f"Found service on Port {sys.argv[1]}")
    #         print(f"[+] PID: {pid[0]}")
    #         print(f"[+] Status: {pid[1]}")
    #         ch = input("Wanna Close: (y/n) ")
    #         if ch.lower() == 'y':
    #             p = psutil.Process(pid[0])
    #             p.terminate()
    pid = get_pid(5001)
    print("Initial",pid)
    if not pid == -1:
        # p = psutil.Process(pid[0])
        # p.terminate()
        # pid = get_pid(5001)
        # print(pid)
        terminate_port_process(5001)
        pid = get_pid(5001)
        print("final",pid)
            

