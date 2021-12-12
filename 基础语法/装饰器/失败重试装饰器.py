# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/12
Last Modified: 2021/7/12
Description: 
"""

# 题目：
# 用装饰器实现一个失败重试功能，要求可以指定重试的次数以及时间间隔。
import functools
import time


def retry(timesss, time_interval):
    def out_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"execute {func.__name__}, if failed will retry {timesss} times")

            retry_times = 0

            while retry_times < timesss:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retry_times += 1
                    print(f"failed. retry {retry_times} ...")
                    time.sleep(time_interval)

                    if retry_times == timesss:
                        # raise Exception("over retry times.")
                        print("over retry times.")

        return wrapper

    return out_wrapper


@retry(5, 1)
def logic_func(a, b, c):
    # 1 / 0

    print(a, b, c)


if __name__ == '__main__':
    logic_func(1, 2, 3)
