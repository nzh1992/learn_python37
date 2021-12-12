# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/11/28
Last Modified: 2020/11/28
Description: 
"""


# 递归特点
# 1. 调用自身
# 2. 结束条件(也叫边界条件)


def recursion1(x):  # 错误，边界条件缺失，导致死循环
    recursion1(x - 1)


def recursion2(x):
    if x < 0:
        return

    print(x)
    recursion2(x - 1)


recursion2(5)