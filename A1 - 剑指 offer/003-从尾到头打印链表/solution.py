#! /usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        """初始化，头结点为空"""
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def append(self, item):
        """尾部添加元素"""
        node = ListNode(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，_head 指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 方法一：递归
    def reverse_digui(self, head: ListNode) -> list:
        return self.reverse_digui(head.next) + [head.val] if head else []

    # 方法二：反转
    def reverse_fanzhuan(self, head: ListNode) -> list:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    # 方法三：堆栈
    def reverse_duizhan(self, head: ListNode) -> list:
        stack = []
        while head:  # push
            stack.append(head.val)
            head = head.next
        res = []
        while stack:  # pop
            res.append(stack.pop(-1))
        return res


def main():
    # 创建链表
    link_list = SingleLinkList()
    for i in range(1, 4, 1):
        link_list.append(i)
    # 从尾到头打印链表 - 递归
    output = link_list.reverse_digui(link_list._head)
    print("递归法：", output)
    # 反转
    output = link_list.reverse_fanzhuan(link_list._head)
    print("反转法：", output)
    # 堆栈
    output = link_list.reverse_duizhan(link_list._head)
    print("堆栈法：", output)


if __name__ == '__main__':
    main()
