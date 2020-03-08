#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 66
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add_on = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i] + add_on
            if tmp > 9:
                add_on = tmp - 9
                tmp -= 10
            else:
                add_on = 0
            digits[i] = tmp
        if add_on != 0:
            tmp = [add_on]
            tmp.extend(digits)
            digits = tmp
        return digits
