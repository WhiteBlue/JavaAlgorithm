# 171

import math

COLUMN_SIZE = 26

class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        for i in range(len(s)):
            times = len(s) - i - 1
            val += int((ord(s[i]) - ord('A') + 1) * math.pow(COLUMN_SIZE, times))
        return val


if __name__ == '__main__':
    s = Solution()

    print(s.titleToNumber('ZY'))
