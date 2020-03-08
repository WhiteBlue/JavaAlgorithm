#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 63
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        arr = [[0 for i in range(0, n)] for i in range(0, m)]

        for x in range(0, m):
            for y in range(0, n):
                tmp = 0
                if obstacleGrid[x][y] != 1:
                    if x == 0 and y == 0:
                        tmp = 1
                    if x - 1 >= 0:
                        tmp += arr[x - 1][y]
                    if y - 1 >= 0:
                        tmp += arr[x][y - 1]
                arr[x][y] = tmp

        return arr[m - 1][n - 1]
