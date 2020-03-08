from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        last_min, last_max, max_prod = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            new_min = min(last_min * nums[i], last_max * nums[i], nums[i])
            new_max = max(last_min * nums[i], last_max * nums[i], nums[i])

            if new_max > max_prod:
                max_prod = new_max
            last_max, last_min = new_max, new_min

        return max_prod


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
