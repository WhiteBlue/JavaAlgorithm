from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_val, right_val = nums[i] - 1, nums[i] - 1
            if i > 0:
                left_val = nums[i - 1]
            if i < len(nums) - 1:
                right_val = nums[i + 1]

            if nums[i] > left_val and nums[i] > right_val:
                return i
        return -1
