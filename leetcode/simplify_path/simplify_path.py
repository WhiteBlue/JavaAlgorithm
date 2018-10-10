#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 71
# Given an absolute path for a file (Unix-style), simplify it.

import string


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = []
        parts = path.split("/")
        for p in parts:
            if p == "." or p == "":
                continue
            elif p == "..":
                if len(arr) > 0:
                    arr.pop()
            else:
                arr.append(p)
        return "/" + string.join(arr, "/")
