package part1.merge_two_sorted_lists;

/**
 * id: 21
 * <p>
 * Merge two sorted linked lists and return it as a new list.
 * The new list should be made by splicing together the nodes of the first two lists.
 */

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class MergeTwoSortedLists {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        //都不为null
        if (l1.val > l2.val) {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        } else {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
    }


    public ListNode mergeTwoListsLoop(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null;
        }
        if (l1 == null || l2 == null) {
            return l1 == null ? l2 : l1;
        }

        ListNode tmp, top;
        if (l1.val > l2.val) {
            top = tmp = l2;
            l2 = l2.next;
        } else {
            top = tmp = l1;
            l1 = l1.next;
        }

        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                tmp.next = l2;
                tmp = l2;
                l2 = l2.next;
            } else {
                tmp.next = l1;
                tmp = l1;
                l1 = l1.next;
            }
        }

        if (l1 != null) {
            tmp.next = l1;
        }
        if (l2 != null) {
            tmp.next = l2;
        }
        return top;
    }


}
