package part1.generate_parentheses;

import java.util.ArrayList;
import java.util.List;

/**
 * id: 22
 * <p>
 * <p>
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 */
public class GenerateParentheses {
    /**
     * 蛋疼的DP方法
     * <p>
     * 关系式:
     * f(0)=""
     * f(1)=["("+f(0)+")"]
     * f(2)=["("+f(0)+")"+f(1)]+["("+f(1)+")"+f(0)]
     * f(3)=["("+f(0)+")"+f(2)]+["("+f(1)+")"+f(1)]+["("+f(2)+")"+f(0)]
     *
     * @param n count
     * @return List
     */
    public List<String> generateParenthesisDP(int n) {
        List<List<String>> list = new ArrayList<>();
        List<String> list0 = new ArrayList<>();
        List<String> list1 = new ArrayList<>();
        list0.add("");
        list1.add("()");

        list.add(0, list0);
        list.add(1, list1);

        for (int i = 2; i <= n; i++) {
            List<String> inner = new ArrayList<>();
            for (int j = 0; j < i; j++) {
                //遍历之前计算结果
                List<String> before0 = list.get(j);
                List<String> before1 = list.get(i - j - 1);
                for (String o0 : before0) {
                    for (String o1 : before1) {
                        inner.add("(" + o0 + ")" + o1);
                    }
                }
            }
            list.add(i, inner);
        }

        return list.get(n);
    }


    private void findIn(List<String> list, int left, int right, int n, String target) {
        if (left == n && right == n) {
            //目标达到
            list.add(target);
            return;
        }
        if (right > left || left > n || right > n) {
            //括号不闭合
            return;
        }

        findIn(list, left + 1, right, n, target + "(");
        findIn(list, left, right + 1, n, target + ")");
    }


    /**
     * 常规Recursion解法
     *
     * @param n count
     * @return rresult
     */
    public List<String> generateParenthesis(int n) {
        List<String> returnList = new ArrayList<>();

        findIn(returnList, 0, 0, n, "");

        return returnList;
    }


}
