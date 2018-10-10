#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 74
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        s0, e0 = 0, len(matrix) - 1
        while s0 <= e0:
            mid = (s0 - e0) / 2 + e0
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                e0 = mid - 1
            else:
                s0 = mid + 1
        line = min(s0, e0)
        s1, e1 = 0, len(matrix[line]) - 1
        while s1 <= e1:
            mid = (s1 - e1) / 2 + e1
            if matrix[line][mid] == target:
                return True
            if matrix[line][mid] > target:
                e1 = mid - 1
            else:
                s1 = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    # print s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    print s.searchMatrix([[1]], 3)
