# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/11/28
Last Modified: 2020/11/28
Description: 继承Thread类
"""
import time
from random import randint
from threading import Thread


class DownloadTask(Thread):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def run(self):
        print(f"开始下载{self._file_name}...")
        time_to_download = randint(5, 10)
        time.sleep(time_to_download)
        print(f"{self._file_name}下载完成, 耗时{time_to_download}s")


if __name__ == '__main__':
    start_time = time.time()

    t1 = DownloadTask('file_1.pdf')
    t1.start()

    t2 = DownloadTask('file_2.pdf')
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()
    print(f"总耗时{end_time - start_time}s")
