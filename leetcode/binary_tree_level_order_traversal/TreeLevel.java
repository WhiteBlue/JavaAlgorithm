package part2.binary_tree_level_order_traversal;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * id: 102
 * <p>
 * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class TreeLevel {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> returnList = new ArrayList<>();
        LinkedList<TreeNode> stack = new LinkedList<>();

        if (root == null) {
            return returnList;
        }

        int printCount = 0;
        int count = -1;
        int nextCount = 0;

        stack.addLast(root);

        List<Integer> list = new ArrayList<>();
        while (!stack.isEmpty()) {
            TreeNode target = stack.removeFirst();

            list.add(target.val);
            count++;

            if (target.left != null) {
                nextCount++;
                stack.addLast(target.left);
            }
            if (target.right != null) {
                nextCount++;
                stack.addLast(target.right);
            }

            if (count == printCount) {
                count = 0;
                printCount = nextCount;
                nextCount = 0;
                returnList.add(list);
                list = new ArrayList<>();
            }
        }

        if (!list.isEmpty()) {
            returnList.add(list);
        }

        return returnList;
    }

}
