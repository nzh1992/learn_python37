# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""


def say_hello(country):
    def wrapper_func(func):
        def wrapper_param(*args, **kwargs):
            if country == 'china':
                print("你好")
            elif country == 'america':
                print("hello")
            else:
                return

            func(*args, **kwargs)

        return wrapper_param
    return wrapper_func


@say_hello('china')
def chinese():
    print("I'm chinese.")


@say_hello('america')
def jack():
    print("I'm jack")


chinese()

jack()
