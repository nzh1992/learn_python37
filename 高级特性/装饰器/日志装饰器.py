# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print("start execute func")

        func(*args, **kwargs)

        print("func execute done")

    return wrapper


@logger
def my_sum(a, b):
    print("count my sum")
    return a + b


result = my_sum(4, 5)
print(result)