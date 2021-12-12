# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""


class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper_param(*args, **kwargs):
            print(f"{self.level} -- function:{func.__name__}() is running.")
            func(*args, **kwargs)

        return wrapper_param


@logger('DEBUG')
def my_function(a, b):
    print("my function")
    print(a + b)


@logger('ERROR')
def my_error_function(a, b):
    print(a + b / 0)


my_function(5, 6)

my_error_function(5, 6)