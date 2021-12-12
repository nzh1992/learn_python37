# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/1/10
Last Modified: 2021/1/10
Description: 
"""
a = 1

def func(a):
    a += 1
    print(a, id(a))

func(a)
print(a, id(a))


b = []
def funcb(b):
    b.append(1)
    print(b, id(b))

funcb(b)
print(b, id(b))

