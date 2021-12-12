# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/15
Last Modified: 2021/7/15
Description: 学习生成器
"""

# 0. 前置知识
# 在学习生成器，需要了解以下内容

# 0.1 什么是迭代器协议？
# 是指对象需要提供next方法，该方法要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代。


# 1. 什么是生成器？
# 生成器是一种并不立即计算的结构模式，它提供了延迟操作，是指在需要的时候才产生结果。


# 2. 创建生成器
def create_generator_by_function():
    """
    通过'生成器函数'创建生成器。

    常规函数定义，但是使用yield语句替代return语句返回结果。yield语句一次返回一个结果，
    在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行。
    """
    def gen_squares(n):
        for i in range(n):
            yield i ** 2
            print("come back")

    for item in gen_squares(5):
        print(item)


def create_generator_by_expression():
    """
    通过 '生成器表达式' 创建生成器.

    生成器表达式 和 列表推导式 很像，就是将[] 换成 ()
    """
    squares = (x ** 2 for x in range(5))

    for item in squares:
        print(item)


# 3. 体验延迟特性
# 3.1 使用sum函数，进行1-10延迟就和
def sum_delay():
    numbs = (x for x in range(1, 11, 1))

    total = sum(numbs)
    print(total)


# 4. 注意事项
# 你必须清楚，生成器只能使用一次！！！


if __name__ == '__main__':
    create_generator_by_expression()

