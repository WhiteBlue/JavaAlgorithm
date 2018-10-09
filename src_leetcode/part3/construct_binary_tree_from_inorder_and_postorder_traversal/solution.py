#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 106
# Given inorder and postorder traversal of a tree, construct the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.i = 1
        self.j = 1

    def build_tree(self, in_order, post_order, left):
        if self.i == len(in_order):
            return left

        top = TreeNode(in_order[self.i])
        self.i += 1

        if in_order[self.i] != post_order[self.j]:


