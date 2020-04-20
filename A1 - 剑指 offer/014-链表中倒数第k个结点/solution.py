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

    def items_kth_from_end(self, node):
        """从节点 node 遍历链表"""
        cur = node
        # 循环遍历
        while cur is not None:
            yield cur.val  # 返回生成器
            cur = cur.next

    # 方法一：遍历
    def get_kth_from_end_by_bianli(self, head: ListNode, k: int) -> ListNode:
        if k <= 0:
            return None
        count, node = 0, head
        while node:
            count += 1
            node = node.next
        if k > count:
            return None
        node, n = head, count - k
        for _ in range(n):
            node = node.next
        return node

    # 方法二：双指针
    def get_kth_from_end_by_zhizhen(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        if (not head) or (k == 0):   # 考虑特殊情况 1、3
            return None
        for _ in range(k):  # 考虑特殊情况 2
            if former:
                former = former.next
            else:
                return None
        while former:
            former, latter = former.next, latter.next
        return latter


def main():
    # 创建链表
    link_list = SingleLinkList()
    for i in range(1, 6, 1):
        link_list.append(i)

    # 遍历
    node = link_list.get_kth_from_end_by_zhizhen(link_list._head, 2)
    for i in link_list.items_kth_from_end(node):
        print(i, end='\t')

    print('\n')

    # 双指针
    latter = link_list.get_kth_from_end_by_zhizhen(link_list._head, 2)
    for i in link_list.items_kth_from_end(latter):
        print(i, end='\t')


if __name__ == "__main__":
    main()
