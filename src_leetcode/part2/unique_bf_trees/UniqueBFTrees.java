package part2.unique_bf_trees;

/**
 * id: 96
 * <p>
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 */
public class UniqueBFTrees {

    /**
     * DP
     *
     * @param n num
     * @return int
     */
    private int countDP(int n) {
        int[] array = new int[n + 1];
        array[0] = 1;
        array[1] = 1;
        for (int i = 2; i <= n; i++) {
            int count = 0;
            for (int j = 0; j < i; j++) {
                count += array[j] * array[i - 1 - j];
            }
            array[i] = count;
        }
        return array[n];
    }

    /**
     * 递归
     *
     * @param n num
     * @return int
     */
    private int countTree(int n) {
        if (n <= 1) {
            return 1;
        }
        int back = 0;
        for (int i = 0; i < n; i++) {
            back += countTree(i) * countTree(n - i - 1);
        }
        return back;
    }


}
