#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 92
# Reverse a linked list from position m to n. Do it in-place and in one-pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        self.end = None
        return self.reverse(None, None, m, n, head, 1)

    def reverse(self, pre, start, m, n, node, i):
        if i == m - 1:
            pre = node
        elif i == m:
            start = node
        elif i == n:
            self.end = node
            if pre is not None:
                pre.next = node
            start.next = node.next
            return node
        ret = self.reverse(pre, start, m, n, node.next, i + 1)
        if i >= m:
            ret.next = node
        if i == 1 and m == 1:
            return self.end
        return node


