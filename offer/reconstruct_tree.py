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
    def build_tree(self, pre, tin, start_pre, end_pre, start_tin, end_tin):
        if start_pre == end_pre or start_tin == end_tin:
            return None
        root = TreeNode(pre[start_pre])
        for i in range(start_tin, end_tin):
            if tin[i] == pre[start_pre]:
                # 左子树
                root.left = self.build_tree(pre, tin, start_pre + 1, start_pre + i - start_tin + 1, start_tin, i)
                root.right = self.build_tree(pre, tin, start_pre + i - start_tin + 1, end_pre, i + 1, end_tin)
        return root

    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        return self.build_tree(pre, tin, 0, len(pre), 0, len(tin))
