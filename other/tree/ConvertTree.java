package tree;

import linkedlist.LinkedNode;

import java.util.LinkedList;

/**
 * 二叉树转换问题
 */
public class ConvertTree {

    /**
     * 二叉搜索树转换为链表, 中序遍历创建结构
     *
     * @param root top node
     */
    public static LinkedNode convertTreeToLinkedList(TreeNode root) {
        TreeNode tmp = root;

        LinkedList<TreeNode> list = new LinkedList<>();

        LinkedNode temNode = null;
        LinkedNode topNode = null;

        while (tmp != null || !list.isEmpty()) {
            //左子树向下
            while (tmp != null) {
                list.push(tmp);
                tmp = tmp.leftChild;
            }

            while (!list.isEmpty()) {
                TreeNode target = list.pop();
                System.out.print(target.value + ",");

                if (temNode == null) {
                    //根节点创建
                    topNode = temNode = new LinkedNode(target.value);
                } else {
                    //链接节点
                    LinkedNode newNode = new LinkedNode(target.value);
                    temNode.next = newNode;
                    temNode = newNode;
                }

                if (target.rightChild != null) {
                    tmp = target.rightChild;
                    break;
                }
            }
        }
        return topNode;
    }


    /**
     * 求二叉树镜像
     *
     * @param node top
     * @return result
     */
    public void getMirror(TreeNode node) {
        if (node == null) {
            return;
        }

        getMirror(node.leftChild);
        getMirror(node.rightChild);

        TreeNode tmp = node.leftChild;
        //交换子节点
        node.leftChild = node.rightChild;
        node.rightChild = tmp;
    }


    /**
     * 反转二叉树,非递归(其实就和遍历同原理)
     *
     * @param node top
     */
    public void getMirrorLoop(TreeNode node) {
        if (node == null) {
            return;
        }
        LinkedList<TreeNode> list = new LinkedList<>();
        list.push(node);

        while (!list.isEmpty()) {
            TreeNode tmp = list.pop();

            TreeNode mid = tmp.leftChild;
            tmp.leftChild = tmp.rightChild;
            tmp.rightChild = mid;

            if (tmp.leftChild != null) {
                list.push(tmp.leftChild);
            }
            if (tmp.rightChild != null) {
                list.push(tmp.rightChild);
            }
        }
    }
}
