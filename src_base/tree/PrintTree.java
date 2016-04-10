package tree;

import java.util.LinkedList;

/**
 * 二叉树各种遍历
 */
public class PrintTree {

    /**
     * 前序遍历,无脑递归
     *
     * @param node top node
     */
    public static void frontPrint(TreeNode node) {
        if (node == null) {
            return;
        }

        System.out.print(node.value + ",");

        frontPrint(node.leftChild);
        frontPrint(node.rightChild);
    }

    /**
     * 中序遍历,同样无脑递归
     *
     * @param node top node
     */
    public void middlePrint(TreeNode node) {
        if (node == null) {
            return;
        }

        middlePrint(node.leftChild);
        System.out.print(node.value + ",");
        middlePrint(node.rightChild);
    }

    /**
     * 后序遍历
     *
     * @param node top node
     */
    public void endPrint(TreeNode node) {
        if (node == null) {
            return;
        }

        endPrint(node.leftChild);
        endPrint(node.rightChild);
        System.out.print(node.value + ",");
    }


    /**
     * 前序遍历,循环写法
     *
     * @param top top node
     */
    public void frontPrintLoop(TreeNode top) {
        LinkedList<TreeNode> list = new LinkedList<>();
        list.push(top);

        while (!list.isEmpty()) {
            TreeNode node = list.pop();

            if (node == null) {
                continue;
            }

            System.out.print(node.value + ",");

            list.push(node.rightChild);
            list.push(node.leftChild);
        }
    }


    /**
     * 中序遍历,循环,基本思路逆向打印
     *
     * @param top top node
     */
    public void middlePrintLoop(TreeNode top) {
        LinkedList<TreeNode> list = new LinkedList<>();

        TreeNode tmp = top;

        while (tmp != null || !list.isEmpty()) {
            while (tmp != null) {
                //左子树压入栈
                list.push(tmp);
                tmp = tmp.leftChild;
            }
            while (!list.isEmpty()) {
                TreeNode print = list.pop();
                System.out.print(print.value + ",");
                tmp = print.rightChild;
                //将当前元素置为右子节点
                if (tmp != null) {
                    break;
                }
            }
        }
    }


    /**
     * 按层打印二叉树
     *
     * @param top top node
     */
    public void PrintTreeByLevel(TreeNode top) {
        LinkedList<TreeNode> list = new LinkedList<>();

        list.addLast(top);

        while (!list.isEmpty()) {
            TreeNode node = list.removeFirst();

            System.out.print(node.value + ",");

            if (node.leftChild != null) {
                list.addLast(node.leftChild);
            }

            if (node.rightChild != null) {
                list.addLast(node.rightChild);
            }
        }
    }
}
