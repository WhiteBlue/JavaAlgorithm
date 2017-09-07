#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 104
# Given a binary tree, find its maximum depth.s
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursion(root, 0)

    def recursion(self, root, count):
        if root is None:
            return count
        return max(self.recursion(root.left, count + 1), self.recursion(root.right, count + 1))
