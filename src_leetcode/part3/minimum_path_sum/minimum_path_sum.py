#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 64
# Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom right which minimizes the sum of all numbers along its path.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        tmp = [[0 for _ in range(0, n)] for _ in range(0, m)]
        for x in range(0, m):
            for y in range(0, n):
                val_min = 0
                if x - 1 >= 0 and y - 1 >= 0:
                    val_min = min(tmp[x - 1][y], tmp[x][y - 1])
                else:
                    if x - 1 >= 0:
                        val_min = tmp[x - 1][y]
                    if y - 1 >= 0:
                        val_min = tmp[x][y - 1]
                val_min += grid[x][y]
                tmp[x][y] = val_min
        return tmp[m - 1][n - 1]
