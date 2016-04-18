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

        //遍历链表
        while (next != null) {
            //交换两值
            LinkedNode cache = next;
            next = next.next;
            cache.next = tmp;
            tmp = cache;
        }

        return tmp;
    }


    private LinkedNode reverseRe(LinkedNode top, LinkedNode next) {
        next.next = top;
        if (next.next == null) {
            return next;
        } else {
            return reverseRe(top.next, next.next);
        }
    }

    /**
     * 递归法倒置
     *
     * @param top 首节点
     * @return result
     */
    public LinkedNode reverseRecursion(LinkedNode top) {
        if (top == null) {
            return null;
        }
        if (top.next == null) {
            return top;
        }
        LinkedNode back = this.reverseRe(top, top.next);
        top.next = null;
        return back;
    }


}
