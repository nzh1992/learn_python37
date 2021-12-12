# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""
import time


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()

        func(*args, **kwargs)

        print(f"{func.__name__} 执行了{time.time() - t1}s")

    return wrapper

@timer
def my_calculate():
    total = 0
    for i in range(1000000):
        total += i

    time.sleep(5)
    return total


my_calculate()



