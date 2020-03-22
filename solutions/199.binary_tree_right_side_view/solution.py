# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = []
        ret = []
        curr_counter, next_counter = 0, 0
        if root:
            q.append(root)
            curr_counter = 1
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                next_counter += 1
            if node.right:
                q.append(node.right)
                next_counter += 1

            curr_counter -= 1
            if curr_counter == 0:
                curr_counter, next_counter = next_counter, 0
                ret.append(node.val)

        return ret
