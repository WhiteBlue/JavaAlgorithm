package tree;

/**
 * 二叉树节点
 *
 * 满二叉树性质:
 *      节点数(层树为n): 2^n-1
 *
 */
public class TreeNode {
    public int value;
    public TreeNode leftChild;
    public TreeNode rightChild;

    public TreeNode(int value, TreeNode leftChild, TreeNode rightChild) {
        this.value = value;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public TreeNode(int value) {
        this.value = value;
    }
}
