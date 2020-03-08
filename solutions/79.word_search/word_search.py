#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 79
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.


class Solution(object):
    def judge_char(self, board, word, i, x, y):
        if len(word) == i:
            return True
        if x == len(board) or x < 0 or y == len(board[0]) or y < 0:
            return False

        ret = False
        if board[x][y] == word[i]:
            cache = board[x][y]
            board[x][y] = chr(0)
            ret = self.judge_char(board, word, i + 1, x + 1, y) or \
                  self.judge_char(board, word, i + 1, x - 1, y) or \
                  self.judge_char(board, word, i + 1, x, y + 1) or \
                  self.judge_char(board, word, i + 1, x, y - 1)

            board[x][y] = cache

        return ret

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if self.judge_char(board, word, 0, i, j):
                    return True

        return False


