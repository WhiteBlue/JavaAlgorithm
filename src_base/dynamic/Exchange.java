package dynamic;

/**
 * 找零钱问题
 */
public class Exchange {


    /**
     * 暴力递归方式求解
     *
     * @param changes   零钱
     * @param i         index
     * @param addResult 剩余目标值
     * @return int
     */
    public int findWayRecursion(int[] changes, int i, int addResult) {
        //到达目标值
        if (addResult <= 0) {
            if (addResult == 0) {
                return 1;
            } else {
                return 0;
            }
        }

        //无钱可用
        if (i >= changes.length) {
            return 0;
        }

        int method = 0;

        int target = changes[i];

        int all = (int) Math.ceil((double) addResult / target);

        for (int j = 0; j <= all; j++) {
            method += findWayRecursion(changes, i + 1, addResult - target * j);
        }

        return method;
    }

    /**
     * 动态规划方法,空间换时间
     *
     * @param changes   零钱
     * @param addResult 目标值
     * @return int
     */
    public int findWayDP(int[] changes, int addResult) {
        //生成矩阵
        int[][] cache = new int[changes.length][addResult + 1];

        //纵向遍历
        for (int i = 0; i < changes.length; i++) {
            int target = changes[i];
            //横向遍历
            for (int j = 0; j < addResult + 1; j++) {
                if (i == 0 || j == 0) {
                    //左边界或者右边界
                    cache[i][j] = (j % target == 0) ? 1 : 0;
                } else {
                    //计算当前可能性
                    int findResult = 0;
                    //使用target组成j的不同可能
                    for (int k = 0; target * k <= j; k++) {
                        findResult += cache[i - 1][j - target * k];
                    }
                    cache[i][j] = findResult;
                }
            }
        }
        return cache[changes.length - 1][addResult];
    }


}