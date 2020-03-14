class Solution:
    def numSquares(self, n: int) -> int:
        tmp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            square_num = int(i ** (1 / 2))
            if square_num ** 2 == i:
                tmp[i] = 1
            else:
                min_val = 1 + tmp[i - square_num ** 2]
                for j in range(1, square_num):
                    new_val = 1 + tmp[i - j ** 2]
                    if min_val > new_val:
                        min_val = new_val
                tmp[i] = min_val
        return tmp[n]


if __name__ == '__main__':
    s = Solution()

    print(s.numSquares(3602))
