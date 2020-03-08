class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(15))
