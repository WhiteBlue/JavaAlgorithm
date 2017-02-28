#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        if pHead1.val < pHead2.val:
            head = pHead1
            head.next = self.Merge(pHead1.next, pHead2)
        else:
            head = pHead2
            head.next = self.Merge(pHead1, pHead2.next)

        return head
