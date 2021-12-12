# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/12
Last Modified: 2021/7/12
Description: 日志装饰器
"""


# 装饰器目的：
# 在函数执行前和执行后分别输出一条执行记录，并在执行完成的记录中输出函数的执行时间。

import time


def recoder(func):
    def wrapper():
        print(f"start execute {func.__name__}")
        start = time.time()
        func()
        end = time.time()
        print(f"Done. Use {end - start}s.")
        print("-" * 60)

    return wrapper


@recoder
def query_user_name():
    print("query_user_name")


@recoder
def query_user_address():
    print("query_user_address")


if __name__ == '__main__':
    query_user_name()

    query_user_address()
