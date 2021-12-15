# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/12/12
Last Modified: 2021/12/12
Description: 并发测试
"""
import time
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            print(f"当前账号有{self._balance}元")
            time.sleep(1)
            self._balance = new_balance
            print(f"添加了{money}元，现在为{new_balance}元")
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self) -> None:
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []

    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"账户余额为{account.balance}元")


if __name__ == '__main__':
    main()