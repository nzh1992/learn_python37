# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/11/8
Last Modified: 2020/11/8
Description: Singly Linked List
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node(data={self.data})"


class SinglyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("超出链表范围！")

        p = self.head
        for i in range(index):
            p = p.next

        return p

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise ValueError("超出链表范围！")

        new_node = Node(data)
        if self.size == 0:
            # 当链表为空时
            self.head = new_node
            self.last = new_node
        elif index == 0:
            # 当插入到头部时
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            # 当插入到尾部时
            self.last.next = new_node
            self.last = new_node
        else:
            # 当插入到中间时
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            prev_node.next = new_node

        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围！")

        if index == 0:
            rm_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            pre_node = self.get(index - 1)
            rm_node = pre_node.next
            pre_node.next = None
            self.last = pre_node
        else:
            pre_node = self.get(index - 1)
            next_node = pre_node.next.next
            rm_node = pre_node.next
            pre_node.next = next_node

        self.size -= 1
        return rm_node

    def travel(self, reverse=False):
        if not reverse:
            # 遍历链表
            # 预期输出: 1,2,3,4
            start_node = l.head     # 记录头结点，用于遍历后恢复头结点
            while l.head:
                print(l.head.data)
                l.head = l.head.next

            self.head = start_node

    def reverse_v1(self, head):
        """递归版"""
        if not head:
            return None

        if not head.next:
            return head

        head_node = self.reverse_v1(head.next)
        head.next.next = head
        head.next = None

        print(head)
        return head_node



if __name__ == '__main__':
    # 构造测试链表
    # linked list: 1,2,3,4
    l = SinglyLinkedList()
    l.insert(0, 1)
    l.insert(1, 2)
    l.insert(2, 3)
    l.insert(3, 4)

    l.travel()

    # 根据索引，获取数据
    node = l.get(3)
    # print(node.data)

    # 反转链表
    l.reverse_v1(l.head)



