# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        pre = None
        arr = []
        count_now = 1
        count_next = 0

        if root:
            arr.append(root)
        while len(arr) != 0:
            n = arr.pop(0)

            if n.left:
                arr.append(n.left)
                count_next += 1
            if n.right:
                arr.append(n.right)
                count_next += 1

            count_now -= 1

            if pre:
                pre.next = n
            if count_now != 0:
                pre = n
            else:
                pre = None
                count_now = count_next
                count_next = 0


