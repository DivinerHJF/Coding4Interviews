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

    # 迭代法
    def merge_two_lists_diedai(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while (l1 and l2):
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

    # 递归法
    def merge_two_lists_digui(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_two_lists_digui(l1.next, l2)
            return l1
        l2.next = self.merge_two_lists_digui(l1, l2.next)
        return l2


def main():
    # 创建链表
    list1 = SingleLinkList()
    list2 = SingleLinkList()
    list3, list4 = [1, 3, 4, 5], [1, 2, 4]
    for i in list3:
        list1.append(i)
    for i in list4:
        list2.append(i)
    # 迭代法
    # cur = list1.merge_two_lists_diedai(list1._head, list2._head)
    # 递归法
    cur = list1.merge_two_lists_digui(list1._head, list2._head)
    while cur is not None:
        print(cur.val, end='\t')
        cur = cur.next


if __name__ == "__main__":
    main()
