#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 101
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return self.compare(left.left, right.right) and self.compare(left.right, right.left)
