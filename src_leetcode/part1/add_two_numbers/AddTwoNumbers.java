package part1.add_two_numbers;


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class AddTwoNumbers {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int tmp = 0;
        ListNode pre = null;
        ListNode top = null;
        //遍历相加
        while (l1 != null || l2 != null) {
            int val1 = (l1 == null) ? 0 : l1.val;
            int val2 = (l2 == null) ? 0 : l2.val;

            int value = val1 + val2 + tmp;
            if (value >= 10) {
                tmp = 1;
                value -= 10;
            } else {
                tmp = 0;
            }
            if (pre == null) {
                //新建头节点
                pre = new ListNode(value);
                top = pre;
            } else {
                ListNode tmpNode = new ListNode(value);
                pre.next = tmpNode;
                pre = tmpNode;
            }

            l1 = (l1 == null) ? null : l1.next;
            l2 = (l2 == null) ? null : l2.next;
        }

        //处理最后进位
        if (tmp != 0) {
            pre.next = new ListNode(1);
        }

        return top;
    }
}
