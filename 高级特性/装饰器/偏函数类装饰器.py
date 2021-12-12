# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/12/29
Last Modified: 2020/12/29
Description: 
"""
import time
import functools


class DelayFunc(object):
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"wait for {self.duration} seconds.")
        time.sleep(self.duration)

        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print("call without delay.")
        return self.func(*args, **kwargs)


def delay(duration):
    return functools.partial(DelayFunc, duration)


@delay(duration=5)
def my_add(a, b):
    return a + b


c = my_add(1, 3)
print(c)
