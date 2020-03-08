#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 103
# Given preorder and inorder traversal of a tree, construct the binary tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            head = TreeNode(preorder.pop(0))
            i = inorder.index(head.val)
            head.left = self.buildTree(preorder, inorder[:i])
            head.right = self.buildTree(preorder, inorder[i + 1:])
            return head


