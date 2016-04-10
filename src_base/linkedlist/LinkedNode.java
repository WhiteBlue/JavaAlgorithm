package linkedlist;

/**
 * Description:
 * <p>
 * ======================
 * by WhiteBlue
 * on 16/4/3
 */
public class LinkedNode {
    public int value;
    public LinkedNode next;

    public LinkedNode(int value) {
        this.value = value;
    }

    public LinkedNode(int value, LinkedNode next) {
        this.value = value;
        this.next = next;
    }
}
