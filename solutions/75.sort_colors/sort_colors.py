#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 75
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        while i < j:
            while nums[i] == 0 and i < j:
                i += 1
            while nums[j] != 0 and i < j:
                j -= 1
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j -= 1
        j = len(nums) - 1
        while i < j:
            while nums[i] != 2 and i < j:
                i += 1
            while nums[j] == 2 and i < j:
                j -= 1
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j -= 1
