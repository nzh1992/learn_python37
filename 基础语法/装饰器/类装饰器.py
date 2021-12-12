# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/15
Last Modified: 2021/7/15
Description: 
"""


class A:
    def __init__(self):
        print("a init")


def decorator(cls):
    return A


@decorator
class Model:
    def __init__(self):
        print("Model init")


if __name__ == '__main__':
    m = Model()
    print(m)

