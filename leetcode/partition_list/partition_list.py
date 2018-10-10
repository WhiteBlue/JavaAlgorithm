#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 86
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less, more, tmp_less, tmp_more = None, None, None, None
        while head is not None:
            if head.val < x:
                if less is None:
                    less, tmp_less = head, head
                else:
                    less.next = head
                    less = head
            else:
                if more is None:
                    more, tmp_more = head, head
                else:
                    more.next = head
                    more = head
            head = head.next
        if more is not None:
            more.next = None
        if less is None:
            return tmp_more
        else:
            less.next = tmp_more
            return tmp_less
