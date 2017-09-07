#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 103
#  Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
#  then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tmp = []
        next_count = 0
        now_count = 1
        reverse = False

        if root is not None:
            tmp.append(root)
        result = []
        tmp_result = []

        while len(tmp) > 0:
            target = tmp.pop(0)

            tmp_result.append(target.val)

            if target.left is not None:
                tmp.append(target.left)
                next_count += 1
            if target.right is not None:
                tmp.append(target.right)
                next_count += 1

            now_count -= 1
            if now_count == 0:
                now_count = next_count
                next_count = 0
                if reverse:
                    tmp_result.reverse()
                reverse ^= True
                result.append(tmp_result)
                tmp_result = []
        return result
