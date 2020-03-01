class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = []
        while n > 0:
            n -= 1
            div, mod = divmod(n, 26)
            ret.append(chr(ord('A') + mod))
            n = div
        return ''.join(ret[::-1])


if __name__ == '__main__':
    s = Solution()

    print(s.convertToTitle(701))
