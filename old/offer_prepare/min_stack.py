#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class Solution:
    def __init__(self):
        self._last = None

    def push(self, node):
        if self._last is None:
            self._last = Node(node)
        else:
            new_node = Node(node)
            self._last.next = new_node
            new_node.pre = self._last
            self._last = new_node

    def pop(self):
        last_node = self._last
        self._last = last_node.pre
        if self._last is not None:
            self._last.next = None
        return last_node.val

    def top(self):
        return self._last.val

    def min(self):
        n = self._last
        min_val = None
        while n is not None:
            if min_val is None or n.val < min_val:
                min_val = n.val
            n = n.pre
        return min_val
