package part1.regular_expression_matching;

/**
 * id: 10
 * <p>
 * Implement regular expression matching with support for '.' and '*'.
 */ e
public class Solution {

    //@todo not passed
    public boolean isMatch(String s, String p) {
        int iEnd = s.length() - 1;
        int jEnd = p.length() - 1;
        //从后向前
        while (iEnd >= 0 && jEnd >= 0 && (s.charAt(iEnd) == p.charAt(jEnd) || p.charAt(jEnd) == '.')) {
            if (p.charAt(jEnd) == '*') {
                //遇到通配符
                break;
            }
            iEnd--;
            jEnd--;
        }
        if (jEnd > 0 && p.charAt(jEnd) == '*') {
            jEnd -= 2;
        }
        if ((iEnd < 0 || jEnd < 0) && (iEnd != jEnd)) {
            return false;
        }
        int i = 0, j = 0;
        //从前向后
        while (i <= iEnd && j <= jEnd) {
            if ((j + 1 <= jEnd) && p.charAt(j + 1) == '*') {
                //遇到通配符
                while (i <= iEnd && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.')) {
                    i++;
                }
                j += 2;
                continue;
            }
            if (p.charAt(j) != '.' && s.charAt(i) != p.charAt(j)) {
                return false;
            }
            i++;
            j++;
        }
        return !(i <= iEnd || j <= jEnd);
    }
}

