# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        arr = sorted(arr)
        root = None
        pre = None
        for num in arr:
            node = ListNode(num)
            if pre:
                pre.next = node
                pre = node
            if not root:
                root = node
        return root
