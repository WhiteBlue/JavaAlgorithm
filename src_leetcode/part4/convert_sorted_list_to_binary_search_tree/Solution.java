/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode buildTree(List<Integer> arr, int start, int end) {
        if(start>end){
            return null;
        }
        if (start == end) {
            return new TreeNode(arr.get(start));
        }
        int mid = (start + end) / 2;
        TreeNode left = this.buildTree(arr, start, mid-1);
        TreeNode node = new TreeNode(arr.get(mid));
        TreeNode right = this.buildTree(arr, mid + 1, end);
        node.left = left;
        node.right = right;

        return node;
    }

    public TreeNode sortedListToBST(ListNode head) {
        List<Integer> tmp = new ArrayList<Integer>();
        ListNode node = head;
        while (node != null) {
            tmp.add(node.val);
            node = node.next;
        }

        if (tmp.size() == 0) {
            return null;
        }


        return this.buildTree(tmp, 0, tmp.size()-1);
    }
}
