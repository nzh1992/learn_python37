# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/12
Last Modified: 2021/7/12
Description: 
"""


def recorder(func):
    def wrapper():
        print(f"execute {func.__name__}")
        result = func()
        return result

    return wrapper


@recorder
def calculate():
    a = 10
    b = 20
    return a + b


if __name__ == '__main__':
    c = calculate()
    print(c)