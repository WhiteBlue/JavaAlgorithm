package part1.swap_nodes_in_pairs;

/**
 * id: 24
 * <p>
 * Given a linked list, swap every two adjacent nodes and return its head.
 */

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class SwapNodesInPairs {


    private ListNode reverseDouble(ListNode nodeA, ListNode nodeB) {
        //只有一点直接返回
        if (nodeB == null) {
            return nodeA;
        }
        //交换两节点
        ListNode nextB = nodeB.next;
        nodeB.next = nodeA;
        if (nextB == null) {
            //不存在下一次交换
            nodeA.next = null;
            return nodeB;
        }
        //设定下一节点
        nodeA.next = reverseDouble(nextB, nextB.next);
        return nodeB;
    }

    /**
     * 递归交换
     *
     * @param head top
     * @return result
     */
    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return head;
        }
        ListNode newHead = head.next;
        reverseDouble(head, newHead);
        return newHead;
    }

}
