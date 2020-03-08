# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        self.findIn(root, 0)

        return int(self.result)

    def findIn(self, root, current):
        if not root:
            return
        current *= 10
        current += root.val

        if root.left:
            self.findIn(root.left, current)
        if root.right:
            self.findIn(root.right, current)

        if not root.left and not root.right:
            self.result += current


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    print(s.sumNumbers(root))
