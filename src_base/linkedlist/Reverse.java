package linkedlist;

/**
 * 最基本的链表反转
 */
public class Reverse {


    public LinkedNode reverse(LinkedNode top) {
        if (top == null) {
            return null;
        }
        LinkedNode next = top.next;
        LinkedNode tmp = top;
        //头节点为尾
        tmp.next = null;

        while (next != null) {
            LinkedNode cache = next;
            next = next.next;
            cache.next = tmp;
            tmp = cache;
        }

        return tmp;
    }

}
