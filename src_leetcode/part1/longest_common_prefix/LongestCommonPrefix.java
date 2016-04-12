package part1.longest_common_prefix;


/**
 * id: 14
 * <p>
 * Write a function to find the longest common prefix string amongst an array of strings.
 */
public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        String tmp = (strs.length > 0) ? strs[0] : null;
        int count = (tmp == null) ? 0 : tmp.length() - 1;

        for (int i = 1; i < strs.length; i++) {
            for (int j = 0; j <= count; j++) {
                if (strs[i].length() <= j || strs[i].charAt(j) != tmp.charAt(j)) {
                    //长度不足或者不等
                    count = j - 1;
                }
            }
            //替换tmp
            tmp = strs[i];
        }

        return (tmp == null) ? "" : tmp.substring(0, count + 1);
    }

}
