#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 94
# Given a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        self.find_in(root, list)
        return list

    def find_in(self, node, list):
        if node is None:
            return
        self.find_in(node.left, list)
        list.append(node.val)
        self.find_in(node.right, list)
