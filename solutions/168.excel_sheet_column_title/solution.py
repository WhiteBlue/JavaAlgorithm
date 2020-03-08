COLUMN_SIZE = 26


class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = []
        while n > 0:
            val = int(n % COLUMN_SIZE)
            if val == 0:
                val = 26
            ret.append(chr(ord('A') + val - 1))
            n -= val
            n /= 26
        return ''.join(ret[::-1])


if __name__ == '__main__':
    s = Solution()

    print(s.convertToTitle(28))
