import functools
from typing import List


def compare(x, y):
    if x + y == y + x:
        return 0
    if x + y > y + x:
        return 1
    else:
        return -1


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(x) for x in nums]
        str_nums = sorted(str_nums, key=functools.cmp_to_key(compare), reverse=True)

        if str_nums and str_nums[0] == '0':
            return '0'

        return ''.join(str_nums)
