# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        arr = sorted(arr)
        root = None
        pre = None
        for num in arr:
            node = ListNode(num)
            if not root:
                root = node
            if pre:
                pre.next = node
            pre = node
        return root
