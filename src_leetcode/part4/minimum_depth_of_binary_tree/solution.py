class Solution(object):
    def __init__(self):
        self.min=-1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.findIn(root,1)
        return self.min

    def findIn(self,root,depth):
        if root.left is None and root.right is None:
            if depth<self.min or self.min==-1:
                self.min=depth
        else:
            if root.left is not None:
                self.findIn(root.left,depth+1)
            if root.right is not None:
                self.findIn(root.right,depth+1)
