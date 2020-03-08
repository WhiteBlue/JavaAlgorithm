# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        b = headB
        len_b = 0
        while b:
            b = b.next
            len_b += 1

        a = headA
        len_a = 0
        while a:
            a = a.next
            len_a += 1

        a = headA
        b = headB

        if len_a >= len_b:
            while len_a > len_b:
                a = a.next
                len_a -= 1
        else:
            while len_b > len_a:
                b = b.next
                len_b -= 1

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
