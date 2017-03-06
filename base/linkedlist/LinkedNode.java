package linkedlist;


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
