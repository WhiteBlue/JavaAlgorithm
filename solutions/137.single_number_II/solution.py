from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()
        tmp = 0
        for num in nums:
            val = num + 1
            if val in cache:
                tmp -= val
            else:
                cache.add(val)
                tmp += val * 2

        return int((tmp / 2) - 1)

    def singleNumber_without_space(self, nums: List[int]) -> int:
        ret = 0
        mask = 1
        for i in range(32):
            tmp = 0
            for num in nums:
                tmp += mask & num >> i
            tmp %= 3
            ret += tmp << i
        return ret
