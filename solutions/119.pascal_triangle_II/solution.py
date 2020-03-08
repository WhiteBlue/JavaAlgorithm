from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tmp = [1]
        for i in range(1, rowIndex + 1):
            row = []
            for j in range(0, i + 1):
                result = 0
                if j - 1 >= 0:
                    result += tmp[j - 1]
                if j <= i - 1:
                    result += tmp[j]
                row.append(result)
            tmp = row
        return tmp
