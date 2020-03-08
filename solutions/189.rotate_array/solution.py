from typing import List

# @todo not passed
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == len(nums) - 1:
            k -= 1

        for _ in range(k + 1):
            for i in range(1, len(nums)):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


if __name__ == '__main__':
    s = Solution()

    arr = [1, 2, 3, 4, 5, 6]

    s.rotate(arr, 1)

    print(arr)
