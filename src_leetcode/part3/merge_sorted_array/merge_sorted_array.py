#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 88
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        num = []
        a, b = 0, 0
        for i in range(0, m):
            num.append(nums1[i])

        i = 0
        while a < m and b < n:
            if num[a] > nums2[b]:
                nums1[i] = nums2[b]
                b += 1
            else:
                nums1[i] = num[a]
                a += 1
            i += 1

        while a < m:
            nums1[i] = num[a]
            a += 1
            i += 1

        while b < n:
            nums1[i] = nums2[b]
            b += 1
            i += 1
