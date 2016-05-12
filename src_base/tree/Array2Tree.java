package tree;

/**
 * 二叉树构建
 */
public class Array2Tree {

    public TreeNode buildTree(int[] array) {
        TreeNode[] list = new TreeNode[array.length];
        for (int i = 0; i < array.length; i++) {
            list[i] = (array[i] != -1) ? null : new TreeNode(array[i]);
        }
        for (int i = 0; i < array.length; i++) {
            TreeNode node = list[i];
            node.leftChild = (2 * i > list.length && list[2 * i] != null) ? list[2 * i] : null;
            node.rightChild = (2 * i + 1 > list.length && list[2 * i + 1] != null) ? list[2 * i + 1] : null;
        }
        return list[0] == null ? null : list[0];
    }
}
