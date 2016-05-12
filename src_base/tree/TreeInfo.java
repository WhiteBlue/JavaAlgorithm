package tree;


/**
 * 二叉树的基本属性
 */
public class TreeInfo {

    /**
     * 取得节点个数
     *
     * @param node top
     * @return count
     */
    public int countTree(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return countTree(node.leftChild) + countTree(node.rightChild) + 1;
    }


    /**
     * 取得树的深度
     *
     * @param node top
     * @return count
     */
    public int treeDeep(TreeNode node) {
        if (node == null) {
            return 0;
        }

        //返回左右子树深度
        return Math.max(treeDeep(node.leftChild), treeDeep(node.rightChild)) + 1;
    }


    /**
     * 取得二叉树某层节点数
     *
     * @param node        top node
     * @param targetLevel target level
     * @param n           top floor(1)
     * @return count
     */
    public int countNodeByLevel(TreeNode node, int n, int targetLevel) {
        //空节点返回
        if (node == null) {
            return 0;
        }
        if (targetLevel == n + 1) {
            //到达目标层的下一层返回子节点数
            return 1;
        } else {
            //未到达目标层继续递归
            return countNodeByLevel(node.leftChild, targetLevel, n + 1) + countNodeByLevel(node.rightChild, targetLevel, n + 1);
        }
    }


    /**
     * 求叶节点个数
     *
     * @param node top node
     * @return count
     */
    public int countLeafNode(TreeNode node) {
        if (node == null) {
            return 0;
        }

        if (node.leftChild == null && node.rightChild == null) {
            return 1;
        }

        return countLeafNode(node.leftChild) + countLeafNode(node.rightChild);
    }

}
