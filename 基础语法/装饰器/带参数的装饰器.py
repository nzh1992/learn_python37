# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/12
Last Modified: 2021/7/12
Description: 
"""


def recorder(level):
    def out_wrapper(func):
        def wrapper(*args):
            print(f"execute ..., level is {level}")
            result = func(*args)
            return result

        return wrapper

    return out_wrapper


@recorder(100)
def add(a, b, *args):
    return a + b


if __name__ == '__main__':
    c = add(12, 14, 10)

    print(c)