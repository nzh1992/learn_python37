# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 装饰器函数
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        print("execute decorator")
        return func()

    return wrapper


@decorator
def my_func():
    print("my function.")


my_func()