#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 67
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        tmp, add_on, max_len = "", False, max(len(a), len(b))
        for i in range(0, max_len):
            val_a = a[len(a) - i - 1] if i < len(a) else "0"
            val_b = b[len(b) - i - 1] if i < len(b) else "0"
            if val_a == val_b:
                val = add_on
                add_on = True if val_a == "1" else False
            else:
                val = True ^ add_on
            tmp += "1" if val else "0"
        if add_on:
            tmp += "1"
        return tmp[::-1]
