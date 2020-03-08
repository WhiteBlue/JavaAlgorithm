class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0

        while n > 0:
            num = n // 5
            zeros += num
            n = num

        return zeros

