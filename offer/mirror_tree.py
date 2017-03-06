#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/9/20

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def mirror_tree(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.mirror_tree(node.left)
        self.mirror_tree(node.right)

    def Mirror(self, root):
        self.mirror_tree(root)
        return root
