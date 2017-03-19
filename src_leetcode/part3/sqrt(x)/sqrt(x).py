#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 69
# Given a list, rotate the list to the right by k places, where k is non-negative.


class Solution(object):
    # use newton's iteration method
    # f(n)=x^2-n
    # X2=X1-f(X1)/f'(X1)
    # => X2=(n+X1/n)/2
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        n = float(x / 2)
        while True:
            n1 = float(n + x / n) / 2.0
            if int(n) == int(n1):
                return int(n)
            n = n1
