# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        tmp = [root]
        pre = None
        row_count, now_count = 0, 1
        while len(tmp) > 0:
            curr = tmp.pop(0)
            if curr is None:
                continue
            now_count -= 1
            if pre is not None:
                pre.next = curr
            pre = curr
            if curr.left is not None:
                tmp.append(curr.left)
                row_count += 1
            if curr.right is not None:
                tmp.append(curr.right)
                row_count += 1
            if now_count == 0:
                now_count, row_count = row_count, 0
                pre = None
        return root
