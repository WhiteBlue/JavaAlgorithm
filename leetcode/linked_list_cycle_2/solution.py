# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next

            if slow == fast:
                while head != fast:
                    head = head.next
                    fast = fast.next

                return head





