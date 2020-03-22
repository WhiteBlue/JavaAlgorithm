from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        tmp = [0 for _ in nums]

        for i in range(len(nums)):
            if i == 0:
                tmp[i] = nums[i]
            elif i == 1:
                tmp[i] = max(nums[i], tmp[i - 1])
            else:
                a = nums[i] + tmp[i - 2]
                b = tmp[i - 1]
                tmp[i] = max(a, b)
        if tmp:
            return tmp[len(tmp) - 1]
        return 0
