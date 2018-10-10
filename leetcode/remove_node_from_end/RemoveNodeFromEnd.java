package part1.remove_node_from_end;

/**
 * id: 19
 * <p>
 * Given a linked list, remove the nth node from the end of list and return its head.
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class RemoveNodeFromEnd {
    private ListNode tmp;

    private int removeNode(ListNode node, int n) {
        if (node == null) {
            //末尾节点
            return 0;
        }
        int back = removeNode(node.next, n) + 1;
        if (back == n + 1) {
            node.next = (tmp == null) ? null : tmp.next;
        }
        tmp = node;
        return back;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode tmpPre = head, tmp = head.next, tmpNext = head;
        for (int i = 0; i < n; i++) {
            tmpNext = tmpNext.next;
        }

        if (tmpNext == null ) {
            return (n == 1) ? null : tmp;
        }

        while (tmpNext.next != null) {
            tmpPre = tmpPre.next;
            tmp = tmp.next;
            tmpNext = tmpNext.next;
        }

        tmpPre.next = tmp.next;

        return head;
    }

}
