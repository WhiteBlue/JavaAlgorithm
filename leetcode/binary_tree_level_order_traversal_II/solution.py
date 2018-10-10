#!/usr/bin/env python
# -*- coding: utf-8 -*-

# id: 107
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root:
            tmp = []
            floor = []
            count_next = 0
            count = 1
            tmp.append(root)
            while tmp:
                node = tmp.pop(0)
                if node:
                    if node.left:
                        tmp.append(node.left)
                        count_next += 1
                    if node.right:
                        tmp.append(node.right)
                        count_next += 1
                    floor.append(node.val)
                    if len(floor) == count:
                        ret.append(floor)
                        count = count_next
                        count_next = 0
                        floor = []
        ret.reverse()
        return ret
