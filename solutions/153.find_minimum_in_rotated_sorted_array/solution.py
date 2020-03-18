from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                return nums[i]
        return nums[0]
