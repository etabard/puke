# -*- coding: utf-8 -*-

import psutil


class cpu(object):

    @staticmethod
    def times():
        return psutil.cpu_times()

    @staticmethod
    def percent(interval=1):
        return psutil.cpu_percent(interval=interval)

    @staticmethod
    def times_percent(interval=1):
        return psutil.cpu_times_percent(interval=interval)

    @staticmethod
    def count():
        return psutil.NUM_CPUS


class memory(object):

    @staticmethod
    def virtual():
        return psutil.virtual_memory()

    @staticmethod
    def swap():
        return psutil.swap_memory()


class disk(object):

    @staticmethod
    def partitions():
        return psutil.disk_partitions()

    @staticmethod
    def usage(mount='/'):
        return psutil.disk_usage(mount)

    @staticmethod
    def io():
        return psutil.disk_io_counters()


class network(object):

    @staticmethod
    def io(pernic=True):
        return psutil.network_io_counters(pernic=pernic)


class users(object):

    @staticmethod
    def list():
        return psutil.get_users()


class process(object):
    Process = psutil.Process

    @staticmethod
    def list():
        return psutil.test()

    @staticmethod
    def pids():
        return psutil.get_pid_list()
