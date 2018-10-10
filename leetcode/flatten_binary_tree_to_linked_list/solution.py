# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        tmp = None
        arr = []

        if root is not None:
            arr.append(root)
        while len(arr) != 0:
            n = arr.pop()
            if n.right:
                arr.append(n.right)
            if n.left:
                arr.append(n.left)
            if tmp is None:
                tmp = n
            else:
                tmp.left = None
                tmp.right = n
                tmp = n


