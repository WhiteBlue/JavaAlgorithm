package tree;

import java.util.Collections;
import java.util.LinkedList;

/**
 * 二叉树的序列化,反序列化
 */
public class SerialTree {

    /**
     * 前序遍历序列化二叉树
     *
     * @param top 头节点
     * @return result
     */
    public static String serialTree(TreeNode top) {
        LinkedList<TreeNode> list = new LinkedList<>();

        list.push(top);

        StringBuilder stringBuilder = new StringBuilder();

        while (!list.isEmpty()) {
            TreeNode node = list.pop();

            if (node == null) {
                stringBuilder.append("#,");
                continue;
            }
            stringBuilder.append(node.value).append(',');

            list.push(node.rightChild);
            list.push(node.leftChild);
        }

        return stringBuilder.toString();
    }


    /**
     * 递归反序列化二叉树
     *
     * @param in serial result
     */
    public static TreeNode buildTree(String in) {
        String[] values = in.split(",");

        LinkedList<String> list = new LinkedList<>();

        Collections.addAll(list, values);

        return buildNode(list);
    }

    private static TreeNode buildNode(LinkedList<String> list) {
        if (list.isEmpty()) {
            return null;
        }

        String value = list.removeFirst();

        if (value.equals("#")) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.valueOf(value));
        node.leftChild = buildNode(list);
        node.rightChild = buildNode(list);

        return node;
    }
}
