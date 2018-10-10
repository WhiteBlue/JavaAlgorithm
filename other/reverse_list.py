#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/19


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        if pHead is None:
            return pHead
        p = pHead
        tmp = None
        while p.next is not None:
            next_p = p.next
            i = next_p.next
            next_p.next, p.next = p, tmp
            tmp = next_p
            p = i

        p.next = tmp

        return p
