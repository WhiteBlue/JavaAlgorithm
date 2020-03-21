from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        area_len = int(len(nums) / 2)

        offset = 0
        while (offset + area_len) < len(nums):
            if nums[offset] == nums[offset + area_len]:
                return nums[offset]
            offset += 1

        return -1
