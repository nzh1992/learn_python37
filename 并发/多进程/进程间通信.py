# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/11/28
Last Modified: 2020/11/28
Description: 
"""
import os
import time
from multiprocessing import Process, Queue


def write(queue):
    """
    向队列写入数据

    Args:
        queue: 队列

    Returns:
        None
    """
    print(f"写进程 - {os.getpid()}")
    for value in ['a', 'b', 'c']:
        print(f"放入队列, value={value}")
        queue.put(value)
        time.sleep(3)


def read(queue):
    """
    从队列中读取数据
    Args:
        queue: 队列

    Returns:
        None
    """
    print(f"读进程 - {os.getpid()}")
    while True:
        value = queue.get()
        print(f"读取数据，value={value}")


if __name__ == '__main__':
    queue = Queue()

    process_write = Process(target=write, args=(queue,))
    process_read = Process(target=read, args=(queue,))

    process_write.start()
    process_read.start()

    process_write.join()
    process_read.terminate()
