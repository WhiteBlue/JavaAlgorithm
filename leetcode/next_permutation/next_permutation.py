#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 31
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                a = i - 1
                break
        b = 0
        for i in range(len(nums) - 1, a, -1):
            if nums[i] > nums[a]:
                b = i
                break

        nums[a], nums[b] = nums[b], nums[a]
        self.sort(nums, a + 1, len(nums) - 1)

    def sort(self, nums, a, b):
        for _ in range(a, b):
            for j in range(a, b):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
