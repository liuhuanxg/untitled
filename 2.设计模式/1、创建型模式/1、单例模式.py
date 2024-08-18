# -*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、单例模式.py
"""
"""
单例模式(Singleton Pattern)是一个常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在，当希望在某个系统中只出现一个实例时，单例对象就能派上用场
"""


class Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls.SPDK_IOSTAT_READ_TWICE = 0
            cls.SPDK_ISCSI_CHECK_DIR = "/data"
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_global_config(cls, key):
        if key == "spdk_iscsi_check_dir":
            return cls.SPDK_ISCSI_CHECK_DIR
        elif key == "spdk_iostat_read_twice":
            return cls.SPDK_IOSTAT_READ_TWICE

        return None

    @classmethod
    def set_global_config(cls, key, value):
        if key == "spdk_iscsi_check_dir":
            cls.SPDK_ISCSI_CHECK_DIR = value
        elif key == "spdk_iostat_read_twice":
            cls.SPDK_IOSTAT_READ_TWICE = 1


s1 = Singleton()
s2 = Singleton()
print(id(s1), id(s2))
print(Singleton.get_global_config("spdk_iscsi_check_dir"))
print(Singleton.set_global_config("spdk_iscsi_check_dir", "ddd"))
print(Singleton.get_global_config("spdk_iscsi_check_dir"))
