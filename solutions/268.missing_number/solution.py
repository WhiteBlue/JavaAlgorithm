from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = max(nums)
        div, mod = divmod(size, 10)

        sum_result = 0
        for i in range(div):
            sum_result += (10 * (2 * i + 1) * 4) + (10 * i + 5) + (10 * (i + 1))

        for i in range(div * 10 + 1, div * 10 + mod + 1):
            sum_result += i

        found_zero = False
        for num in nums:
            if num == 0:
                found_zero = True
            sum_result -= num

        if sum_result == 0 and found_zero:
            return size + 1

        return sum_result


if __name__ == '__main__':
    s = Solution()

    print(s.missingNumber([0, 1]))
