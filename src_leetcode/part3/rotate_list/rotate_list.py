#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 61
# Given a list, rotate the list to the right by k places, where k is non-negative.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.pre_node = None
        self.last_node = None
        ret_head = head

        len = self.find_k(head, k + 1)
        if k > len != 0:
            k %= len
            self.find_k(head, k + 1)

        if self.pre_node is not None:
            ret_head = self.pre_node.next
            self.pre_node.next = None
            self.last_node.next = head

        return ret_head

    def find_k(self, node, k):
        if node is None:
            return 0
        ret = self.find_k(node.next, k) + 1
        if ret == k:
            if node.next is not None:
                self.pre_node = node
        elif ret == 1:
            self.last_node = node
        return ret


if __name__ == '__main__':
    n0 = ListNode()

    s = Solution()
