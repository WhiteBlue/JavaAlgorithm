# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        i = head.next
        if not i:
            return False
        j = i.next

        while i is not None and j is not None:
            if i == j:
                return True
            i = i.next
            if j.next is None:
                return False
            j = j.next.next
        return False
