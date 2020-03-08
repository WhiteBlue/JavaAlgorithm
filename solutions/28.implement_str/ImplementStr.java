package part2.implement_str;

/**
 * id: 28
 * <p>
 * Implement strStr().
 * Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack
 */
public class ImplementStr {

    public int strStr(String haystack, String needle) {
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) {
                    //匹配长度到达
                    return i;
                }
                if (i + j == haystack.length()) {
                    //长度不足
                    return -1;
                }
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    //匹配失败
                    break;
                }
            }
        }
    }


    public static void main(String args[]) {
        ImplementStr implementStr = new ImplementStr();

        System.out.println(implementStr.strStr("abcde", "de"));
    }

}
