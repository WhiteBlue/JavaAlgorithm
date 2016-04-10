package part1.longest_substring;

/**
 * id: 3
 * <p>
 * <p>
 * Given a string, find the length of the longest substring without repeating characters.
 * For example, the longest substring without repeating letters for "abcabcbb" is "abc",
 * which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
 */
public class LongestSubstring {

    public int lengthOfLongestSubstring(String s) {
        char[] strs = s.toCharArray();

        if (strs.length == 1) {
            return 1;
        }
        int i = 0, j = 1, max = 0, tmp = 1;

        while (j < strs.length) {
            tmp++;
            //检查重复
            for (int k = i; k < j; k++) {
                if (strs[k] == strs[j]) {
                    i = k + 1;
                    tmp = j - k;
                    break;
                }
            }
            if (tmp > max) {
                max = tmp;
            }
            j++;

        }
        return max;
    }

}
