package part1.longest_palindrome;

import java.util.Arrays;

/**
 * id: 5
 * <p>
 * <p>
 * Given a string S, find the longest palindromic substring in S.
 * You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
 */
public class LongestPalindrome {
    private static int tmpA = 0, tmpB = 1;

    /**
     * 判断字符子串是否回文
     */
    private static void judge(char[] strs, int i, int j) {
        while (i >= 0 && j < strs.length) {
            if (strs[i] == strs[j]) {
                if ((j - i + 1) > (tmpB - tmpA)) {
                    tmpA = i;
                    tmpB = j + 1;

                }
                i--;
                j++;
            } else {
                break;
            }
        }
    }

    public static String longestPalindrome(String s) {
        char[] strs = s.toCharArray();

        for (int i = 0; i < strs.length; i++) {
            judge(strs, i, i);
            judge(strs, i, i + 1);
        }
        return new String(Arrays.copyOfRange(strs, tmpA, tmpB));
    }

}
