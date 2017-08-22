#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 78
# Given a set of distinct integers, nums, return all possible subsets.


class Solution(object):
    def deep_copy(self, arr):
        n_arr = []
        for i in arr:
            n_arr.append(i)
        return n_arr

    def find_in(self, arr, tmp, i):
        if i == len(arr):
            self.ret.append(self.deep_copy(tmp))
            return
        tmp.append(arr[i])
        self.find_in(arr, tmp, i + 1)
        tmp.remove(arr[i])
        self.find_in(arr, tmp, i + 1)

    def amaze_solution(self, nums):
        total = 1 << len(nums)
        ret = []
        for i in range(0, total):
            tmp = []
            for j in range(0, len(nums)):
                if i & (1 << j) == 0:
                    tmp.append(nums[j])
            ret.append(tmp)

        return ret

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # self.ret = []
        # self.find_in(nums, [], 0)
        return self.amaze_solution(nums)

