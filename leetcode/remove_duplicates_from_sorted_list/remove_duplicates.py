#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 83
# Given a sorted linked list, delete all duplicates such that each element appear only once.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node is not None:
            nxt = node.next
            while nxt is not None and nxt.val == node.val:
                nxt = nxt.next
            node.next = nxt
            node = node.next
        return head
