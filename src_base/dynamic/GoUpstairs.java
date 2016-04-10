package dynamic;

/**
 * 经典上台阶问题
 */
public class GoUpstairs {

    /**
     * 暴力递归
     *
     * @param n count
     * @return int
     */
    public static int countRecursion(int n) {
        if (n <= 0) {
            return (n == 0) ? 1 : 0;
        }

        int count = 0;

        count += countRecursion(n - 1);
        count += countRecursion(n - 2);

        return count;
    }

    /**
     * 动态规划
     *
     * @param n count
     * @return int
     */
    public static int countDP(int n) {
        int[] cache = new int[n + 1];
        cache[0] = 1;
        cache[1] = 1;

        //楼梯数
        for (int i = 2; i < n + 1; i++) {
            //当前的来源:i-1和i-2
            //基本关系: f(i)=f(i-1)+f(i-2)
            cache[i] = (cache[i - 1] + cache[i - 2]) % 1000000007;
        }

        return cache[n];
    }

}
