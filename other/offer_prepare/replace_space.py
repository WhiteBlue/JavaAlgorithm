#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        new_str = ""
        for i in range(0, len(s)):
            if s[i] == " ":
                new_str += "%20"
            else:
                new_str += s[i]
