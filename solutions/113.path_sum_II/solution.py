# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.buf = []
        self.result = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.buf.append(root.val)
        if root.left is not None:
            self.pathSum(root.left, sum)
        if root.right is not None:
            self.pathSum(root.right, sum)

        if root.left is None and root.right is None:
            count_val = 0
            for i in self.buf:
                count_val += i
            if count_val == sum:
                ret = []
                for j in self.buf:
                    ret.append(j)
                self.result.append(ret)
        self.buf.pop()
        return self.result

