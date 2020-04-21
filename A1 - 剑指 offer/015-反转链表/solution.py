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

    def reverse(self, head: ListNode) -> ListNode:
        """ 双指针，一个指针用作新生成的一个链表当前节点，另一个指针用于源链表遍历 """
        if not head:
            return None
        pre, cur = head, None
        while pre:
            # 连续赋值语句中等式右边其实都是局部变量，而不是真正的变量值本身
            pre.next, cur, pre = cur, pre, pre.next
        return cur


def main():
    link_list = SingleLinkList()
    for i in range(1, 6, 1):
        link_list.append(i)

    for i in link_list.items(link_list._head):
        print(i, end='\t')

    # 双指针
    cur = link_list.reverse(link_list._head)
    print('\n')
    for i in link_list.items(cur):
        print(i, end='\t')


if __name__ == "__main__":
    main()
