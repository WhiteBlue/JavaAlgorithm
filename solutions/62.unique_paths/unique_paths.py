#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 62
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[1 for i in range(0, n)] for i in range(0, m)]
        for x in range(0, m):
            for y in range(0, n):
                if x == 0 and y == 0:
                    continue
                tmp = 0
                if x - 1 >= 0:
                    tmp += arr[x - 1][y]
                if y - 1 >= 0:
                    tmp += arr[x][y - 1]
                arr[x][y] = tmp

        return arr[m - 1][n - 1]
