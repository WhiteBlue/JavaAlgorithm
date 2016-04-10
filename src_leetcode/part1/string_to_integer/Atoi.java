package part1.string_to_integer;


/**
 * id: 8
 * <p>
 * implement atoi to convert a string to an integer.
 */
public class Atoi {

    public static int myAtoi(String str) {
        long back = 0;
        char[] strs = str.toCharArray();
        if (strs.length == 0) {
            return 0;
        }
        boolean flag = false;
        int start = 0;
        for (; start < strs.length; start++) {
            if (strs[start] >= 48 && strs[start] <= 57) {
                break;
            } else if (strs[start] == '+' || strs[start] == '-') {
                flag = (strs[start] == '-');
                start++;
                break;
            } else if (strs[start] != ' ') {
                return 0;
            }
        }

        for (int i = start; i < strs.length; i++) {
            char obj = strs[i];

            if (obj < 48 || obj > 57) {
                back /= Math.pow(10, strs.length - i);
                break;
            } else {
                obj -= 48;
                back += obj * Math.pow(10, strs.length - i - 1);
            }
        }
        if (flag) {
            back = -back;
        }

        if (back > Integer.MAX_VALUE) {
            back = Integer.MAX_VALUE;
        } else if (back < Integer.MIN_VALUE) {
            back = Integer.MIN_VALUE;
        }

        return (int) back;
    }

}
