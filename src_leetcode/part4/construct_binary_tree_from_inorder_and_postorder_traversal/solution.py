#! /bin/python


# Definition for a binary tree node.
# class TreeNode:
#      def __init__(self, x):
#          self.val = x
#          self.left = None
#          self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.recursion(inorder, postorder)


    def recursion(self, inorder, postorder):
        if len(inorder)==0:
            return None
        end=postorder[len(postorder)-1]
        postorder.remove(end)
        top = TreeNode(end)
        if len(inorder)== 1:
            return top
        for i in range(len(inorder)):
            if inorder[i]==end:
                top.right = self.recursion(inorder[i+1:], postorder)
                top.left = self.recursion(inorder[:i], postorder)
        return top
