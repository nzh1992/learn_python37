# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/7/15
Last Modified: 2021/7/15
Description: 
"""


class A:
    def __init__(self):
        self.numbs = [1, 2, 3, 4, 5]

        self.next_idx = 0

    def __iter__(self):
        return (x for x in self.numbs)

    def __next__(self):
        if self.next_idx >= len(self.numbs):
            self.next_idx = 0

        current_idx = self.next_idx
        self.next_idx += 1
        return self.numbs[current_idx]



if __name__ == '__main__':
    a = A()

    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
