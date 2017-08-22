#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 90
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.inner_add(ret, [], 0, sorted(nums))
        return ret

    def inner_add(self, ret, list, index, nums):
        if index == len(nums):
            ret.append(list)
            return
        clone = []
        clone.extend(list)
        clone.append(nums[index])
        self.inner_add(ret, clone, index + 1, nums)
        if len(list) < 1 or list[len(list) - 1] != nums[index]:
            self.inner_add(ret, list, index + 1, nums)

