# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""


instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print("===1===")
        if cls_name not in instances:
            print("===2===")
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance

        return instances[cls_name]

    return get_instance


@singleton
class User():
    _instance = None

    def __init__(self, name):
        print("===3===")
        self.name = name


u1 = User('aaa')
u2 = User('bbb')
print(id(u1))
print(id(u2))
