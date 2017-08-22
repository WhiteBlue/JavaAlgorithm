#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 91
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# Given an encoded message containing digits, determine the total number of ways to decode it.


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = [1 for i in range(0, len(s) + 1)]
        if len(s) == 0 or s[0] == '0':
            return 0
        if s[0] == '0':
            mem[1] = 0
        for i in range(1, len(s)):
            val = 0
            if 9 < int(s[i - 1:i + 1]) < 27:
                val += mem[i - 1]
            if s[i] != '0':
                val += mem[i]
            mem[i + 1] = val
        return mem[len(s)]
