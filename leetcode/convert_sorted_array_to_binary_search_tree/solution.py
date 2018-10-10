#! /bin/python


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        mid = (start + end) / 2
        left = this.buildTree(nums, start, mid - 1)
        node = TreeNode(nums[mid])
        right = this.buildTree(nums, mid + 1, end)
        node.left = left
        node.right = right

        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        return self.buildTree(nums, 0, len(nums) - 1)
