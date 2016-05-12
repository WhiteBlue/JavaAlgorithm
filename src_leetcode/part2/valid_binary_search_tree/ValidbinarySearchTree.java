package part2.valid_binary_search_tree;

/**
 * id: 98
 * <p>
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class ValidbinarySearchTree {
    private TreeNode tmp;

    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        if (!isValidBST(root.left)) {
            return false;
        }

        if (tmp != null) {
            if (root.val <= tmp.val) {
                return false;
            }
        }
        tmp = root;

        return isValidBST(root.right);
    }


    public TreeNode buildTree(int[] array) {
        TreeNode[] list = new TreeNode[array.length];
        for (int i = 0; i < array.length; i++) {
            list[i] = (array[i] == -1) ? null : new TreeNode(array[i]);
        }
        for (int j = 1; j <= array.length; j++) {
            if (list[j - 1] != null) {
                TreeNode node = list[j - 1];
                node.left = (2 * j <= list.length && list[2 * j - 1] != null) ? list[2 * j - 1] : null;
                node.right = (2 * j + 1 <= list.length && list[2 * j] != null) ? list[2 * j] : null;
            }
        }
        return list[0] == null ? null : list[0];
    }

    public static void main(String args[]) {

        ValidbinarySearchTree validbinarySearchTree = new ValidbinarySearchTree();

//        TreeNode node0 = new TreeNode(98);
//        TreeNode node1 = new TreeNode(-57);
//        TreeNode node2 = new TreeNode(58);
//        TreeNode node3 = new TreeNode(31);
//
//        node0.left = node1;
//        node1.right = node2;
//        node2.left = node3;

//        TreeNode node = validbinarySearchTree.buildTree(new int[]{98, -57, -1, -1, 58, 31});
//        TreeNode node = validbinarySearchTree.buildTree(new int[]{10, 5, 15, -1, -1, 6, 20});
        TreeNode node = validbinarySearchTree.buildTree(new int[]{3, 1, 5, 0, 2, 4, 6});
//        TreeNode node = validbinarySearchTree.buildTree(new int[]{1,1});

        System.out.println(validbinarySearchTree.isValidBST(node));
    }
}
