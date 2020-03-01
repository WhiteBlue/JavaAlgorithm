# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        tmp = dict()

        pre = None
        root = None
        while head:
            node = Node(head.val, None, head.random)
            tmp[head.val] = node
            if pre:
                pre.next = node
            if not root:
                root = node
            pre = node
            head = head.next

        node = root
        while node:
            if node.random and node.random.val in tmp:
                node.random = tmp[node.random.val]
            node = node.next

        return root
