#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):  # 节点类
    """单链表的结点"""

    def __init__(self, item):
        self.item = item    # 数据域，item 用于存放数据元素
        self.next = None    # 指针域，next 指向下一个节点

    # 返回节点的数据
    def get_data(self):
        return self.item

    # 更新节点的数据
    def set_data(self, new_data):
        self.item = new_data

    # 返回后继节点
    def get_next(self):
        return self.next

    # 变更后继节点
    def set_next(self, new_next):
        self.next = new_next


class SingleLinkList(object):  # 单链表类

    def __init__(self):
        """初始化，头结点为空"""
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head    # 初始指针指向 head
        count = 0
        # 指针指向 None 表示到达尾部
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        cur = self._head
        # 循环遍历
        while cur is not None:
            yield cur.item  # 返回生成器
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        node.next = self._head  # 新结点指针指向原头部结点
        self._head = node       # 头部结点指针修改为新结点

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
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

    def insert(self, index, item):
        """指定位置插入元素"""
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # 创建元素结点
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


if __name__ == '__main__':
    """操作链表"""
    link_list = SingleLinkList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')
    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n', list(link_list.items()))
    # 删除链表数据
    link_list.remove(0)
    # 查找链表数据
    print(link_list.find(0))
