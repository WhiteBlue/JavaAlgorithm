package tree;

/**
 * 树的比较
 */
public class CompareTree {


    /**
     * 比较两个二叉树,逐个遍历
     *
     * @param nodeA treeA
     * @param nodeB treeB
     * @return bool
     */
    public boolean compareTwoTree(TreeNode nodeA, TreeNode nodeB) {
        if (nodeA == null && nodeB == null) {
            return true;
        } else if (nodeA == null || nodeB == null) {
            //只有一个为空
            return false;
        } else if (nodeA.value != nodeB.value) {
            //值不等
            return false;
        }
        return compareTwoTree(nodeA.leftChild, nodeB.leftChild) && compareTwoTree(nodeA.rightChild, nodeB.rightChild);
    }
}
