from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []

        for i in range(len(nums)):
            if i == 0:
                l.append(nums[i])
            else:
                l.append(nums[i] * l[i - 1])

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                r.append(nums[j])
            else:
                r.append(nums[j] * r[len(nums) - j - 2])

        ret = []
        for i in range(len(nums)):
            left = i - 1
            right = len(nums) - i - 2
            result = 1
            if left >= 0:
                result *= l[left]
            if 0 <= right < len(r):
                result *= r[right]
            ret.append(result)

        return ret
