#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 60
# Given n and k, return the kth permutation sequence.

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = [i for i in range(1, n + 1)]
        ret = ""

        k -= 1
        while n > 0:
            all = 1
            for i in range(0, n):
                all *= n - i
            part = all / n
            j = k / part
            ret += str(arr[j])
            arr.remove(arr[j])
            k -= j * part
            n -= 1

        return ret


