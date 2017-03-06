#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if len(matrix) == 0:
            return []
        x_start, x_end = 0, len(matrix[0])
        y_start, y_end = 0, len(matrix)

        ret = []
        state = 0

        while True:
            if x_start == x_end or y_start == y_end:
                break
            if state == 0:
                for i in range(x_start, x_end):
                    ret.append(matrix[y_start][i])
                y_start += 1
                state += 1
            elif state == 1:
                for i in range(y_start, y_end):
                    ret.append(matrix[i][x_end - 1])
                x_end -= 1
                state += 1
            elif state == 2:
                for i in range(x_end - 1, x_start - 1, -1):
                    ret.append(matrix[y_end - 1][i])
                y_end -= 1
                state += 1
            elif state == 3:
                for i in range(y_end - 1, y_start - 1, -1):
                    ret.append(matrix[i][x_start])
                x_start += 1
                state = 0

        return ret


if __name__ == '__main__':
    s = Solution()

    target = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

    ret = s.printMatrix(target)

    print ret
