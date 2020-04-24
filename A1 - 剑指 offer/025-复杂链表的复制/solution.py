#! /usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, item):
        self.val = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        """创建头结点"""
        self._head = None

    def append(self, item):
        """ 尾部添加元素 """
        node = ListNode(item)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def items(self, node):
        """ 从节点 node 遍历链表 """
        cur = node
        while cur is not None:
            yield cur.val
            cur = cur.next
