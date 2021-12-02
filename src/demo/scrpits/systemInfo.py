#!/home/laicunyi/anaconda3/envs/ros_test/bin/python3.8
#-*-coding:utf-8-*-

import psutil
from time import sleep


class SystemInfo(object):

    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent()

    @staticmethod
    def get_memory_usage():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_io_performance():
        return psutil.disk_io_counters().read_bytes,psutil.disk_io_counters().write_bytes
        
    @staticmethod
    def get_net_performance():
        return psutil.net_io_counters().bytes_sent,psutil.net_io_counters().bytes_recv
        

if __name__ == '__main__':
    while(1):
        print(SystemInfo.get_io_performance())
        sleep(1)

    