#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_list(self, node, list):
        if node is None:
            return
        self.print_list(node.next, list)
        list.append(node.val)

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ret_list = []
        self.print_list(listNode, ret_list)

        return ret_list
