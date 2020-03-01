from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(0, i + 1):
                result = 0
                if j - 1 >= 0:
                    result += triangle[i - 1][j - 1]
                if j <= i - 1:
                    result += triangle[i - 1][j]
                row.append(result)
            triangle.append(row)
        return triangle

