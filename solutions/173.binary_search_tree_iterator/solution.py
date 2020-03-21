# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.list = []
        self.traversal_tree(root)
        self.index = 0

    def traversal_tree(self, root: TreeNode):
        if not root:
            return
        if root.left:
            self.traversal_tree(root.left)
        self.list.append(root.val)
        if root.right:
            self.traversal_tree(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.list[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index != len(self.list)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == '__main__':
    pass
