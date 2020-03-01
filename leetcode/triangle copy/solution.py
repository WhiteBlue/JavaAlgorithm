from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tmp = []
        height = len(triangle)
        for i in range(0, height):
            row = []
            for j in range(0, i + 1):
                val = triangle[i][j]
                if i - 1 >= 0:
                    if j == 0:
                        val += tmp[i - 1][j]
                    elif j == i:
                        val += tmp[i - 1][j - 1]
                    else:
                        val += min(tmp[i - 1][j], tmp[i - 1][j - 1])
                row.append(val)
            tmp.append(row)
        return min(tmp.pop())
