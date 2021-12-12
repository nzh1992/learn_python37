# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""


class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"{self.func.__name__}() is running.")
        return self.func(*args, **kwargs)


@Logger
def say():
    print("hello")


say()