class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.findIn(root,0,sum)

    def findIn(self,root,val,sum):
        newVal=val+root.val
        if root.left is None and root.right is None:
            if newVal == sum:
                return True
            return False
        else:
            ret=False
            if root.left is not None and self.findIn(root.left,newVal,sum):
                ret=True
            if root.right is not None and self.findIn(root.right,newVal,sum):
                ret=True
            return ret
