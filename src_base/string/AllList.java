package string;

/**
 * 字符串排列问题
 */
public class AllList {


    /**
     * 求字符串的全排列,例如:
     * 输出abc的全部组合:abc, acb, bca, bac, cab, cba
     * <p>
     * 递归解决
     *
     * @param in    str
     * @param start start
     */
    public static void permutationA(String in, int start) {
        //输出字符串
        if (start == in.length()) {
            System.out.print(in + ",");
        }
        char[] strs = in.toCharArray();

        //从start开始交换
        for (int k = start; k < strs.length; k++) {
            char tmp = strs[k];
            strs[k] = strs[start];
            strs[start] = tmp;
            permutationA(new String(strs), start + 1);
        }
    }


}
