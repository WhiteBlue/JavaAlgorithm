package dynamic;


/**
 * 经典的01背包问题
 */
public class Package {
    private int count;
    private int maxWeight;

    private int findIn(int[] w, int[] v, int nowValue, int nowWeight, int index) {
        if (index == count || nowWeight >= maxWeight) {
            return nowValue;
        }
        int weight = w[index];
        int value = v[index];

        return Integer.max(findIn(w, v, nowValue + value, nowWeight + weight, index + 1)
                , findIn(w, v, nowValue, nowWeight, index + 1));
    }


    /**
     * 暴力递归解法
     *
     * @param w   weight
     * @param v   value
     * @param n   count
     * @param cap max
     * @return int
     */
    public int maxValueRecursion(int[] w, int[] v, int n, int cap) {
        this.count = n;
        this.maxWeight = cap;
        return findIn(w, v, 0, 0, 0);
    }


    /**
     * 动态规划解法
     *
     * @param w   weight
     * @param v   value
     * @param n   count
     * @param cap max
     * @return int
     */
    public int maxValueDP(int[] w, int[] v, int n, int cap) {
        int[][] cache = new int[n][cap + 1];

        for (int i = 0; i < n; i++) {
            int weight = w[i], value = v[i];
            for (int j = 0; j < cap + 1; j++) {
                if (i == 0) {
                    //第一排
                    cache[i][j] = (j >= weight) ? value : 0;
                } else {
                    //拿或不拿
                    //基本关系: f(i,j)=max(f(i-1,j),f(i-1,j-weight)+value)
                    cache[i][j] = (j >= weight) ? Math.max(cache[i - 1][j], cache[i - 1][j - weight] + value) : cache[i - 1][j];
                }
            }
        }

        return cache[n - 1][cap];
    }


}


