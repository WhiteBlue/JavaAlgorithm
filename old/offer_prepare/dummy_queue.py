#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20
from collections import deque


class Solution:
    def __init__(self):
        self._list = deque()
        self._tmp = deque()
        pass

    def _list2tmp(self):
        while len(self._list) > 0:
            self._tmp.append(self._list.pop())

    def _tmp2list(self):
        while len(self._tmp) > 0:
            self._list.append(self._tmp.pop())

    def push(self, node):
        if len(self._tmp) > 0:
            self._tmp2list()
        self._list.append(node)

    def pop(self):
        if len(self._tmp) == 0:
            self._list2tmp()
        return self._tmp.pop()


if __name__ == '__main__':
    s = Solution()

    for i in range(0, 10):
        s.push(i)

    for j in range(0, 10):
        print s.pop()
