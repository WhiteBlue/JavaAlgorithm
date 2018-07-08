#! /bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ret=True


    def isBalanced(self, root):
        self.findIn(root,0)
        return self.ret


    def findIn(self,root,depth):
        if root is not None:
            depthLeft=self.findIn(root.left,depth+1)
            depthRight=self.findIn(root.right,depth+1)
            if abs(depthRight-depthLeft)>1:
                self.ret=False
            return max(depthLeft,depthRight)
        else:
            return depth
