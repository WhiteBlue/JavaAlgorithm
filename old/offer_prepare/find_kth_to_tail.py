#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/19


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.target = None

    def find_in(self, n, k):
        if n is None:
            return 0
        ret_val = self.find_in(n.next, k) + 1
        if ret_val == k:
            self.target = n
        return ret_val

    def FindKthToTail(self, head, k):
        self.find_in(head, k)
        return self.target
