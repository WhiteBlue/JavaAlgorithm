#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 93
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

import string


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        if len(s) <= 12:
            self.findIn("", "", s, 0, 0)
        return self.result

    def findIn(self, target, val, s, i, p):
        if i == len(s):
            if p == 3:
                self.result.append(target)
            return
        new_val = val + s[i]
        if val != '0' and string.atoi(new_val) <= 255:
            self.findIn(target + s[i], new_val, s, i + 1, p)
        if len(target) != 0:
            self.findIn(target + "." + s[i], s[i], s, i + 1, p + 1)


if __name__ == '__main__':
    s = Solution()

    ret = s.restoreIpAddresses("010010")

    for i in ret:
        print i
