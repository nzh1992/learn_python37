# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/11/28
Last Modified: 2020/11/28
Description: 
"""
import time
from multiprocessing import Pool
from queue import Queue


def create_queue():
    # 创建一个包含100个任务的队列
    queue = Queue()
    [queue.put(item) for item in range(1, 11)]

    return queue


def worker(data):
    time.sleep(3)
    print(f"处理完成，{data}")


if __name__ == '__main__':
    queue = create_queue()

    pool = Pool(processes=4)

    start_time = time.time()

    while queue.qsize():
        element = queue.get()
        # pool.apply(worker, args=(element,))     # 提交任务后会阻塞，直到任务执行完毕
        pool.apply_async(worker, args=(element,))   # 提交任务后不会阻塞，继续提交其他任务，直到进程池中的进程被占满才会阻塞，待某一进程执行完毕后，进程变为空闲状态，再继续提交任务。

    pool.close()
    pool.join()

    print(f"所有任务执行完毕，耗时: {time.time() - start_time}")
