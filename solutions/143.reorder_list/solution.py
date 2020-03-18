# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        cache = []
        curr = head
        size = 0
        while curr:
            cache.append(curr)
            curr = curr.next
            size += 1
        size = int(size / 2)
        curr = head
        for i in range(size):
            right_node = cache.pop()
            next_ptr = curr.next
            curr.next = right_node
            right_node.next = next_ptr
            curr = next_ptr
        if curr:
            curr.next = None


if __name__ == '__main__':
    a0 = ListNode(0)
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)

    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4

    s = Solution()

    s.reorderList(a0)

    print(a0)
