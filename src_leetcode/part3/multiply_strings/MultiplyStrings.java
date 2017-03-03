/**
 * id: 43
 * <p>
 * Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
 */

public class MultiplyStrings {

    private int char2Int(String in, int i) {
        return in.charAt(i) - 48;
    }

    public String multiply(String num1, String num2) {
        int TMP_LEN = num1.length() + num2.length() + 2;
        int[][] tmp = new int[num2.length()][TMP_LEN];
        for (int i = 0; i < num2.length(); i++) {
            int target = this.char2Int(num2, num2.length() - i - 1);
            int addOn = 0;
            for (int j = 0; j < num1.length(); j++) {
                int val = this.char2Int(num1, num1.length() - j - 1) * target + addOn;
                if (val > 9) {
                    addOn = val / 10;
                    val %= 10;
                } else {
                    addOn = 0;
                }
                tmp[i][TMP_LEN - i - j - 1] = val;
            }
            if (addOn != 0) {
                tmp[i][TMP_LEN - i - num1.length() - 1] = addOn;
            }
        }

        StringBuilder sb = new StringBuilder();
        int addOn = 0;
        for (int j = TMP_LEN - 1; j >= 0; j--) {
            int val = 0;
            for (int i = 0; i < num2.length(); i++) {
                val += tmp[i][j];
            }
            val += addOn;
            if (val > 9) {
                addOn = val / 10;
                val %= 10;
            } else {
                addOn = 0;
            }
            sb.append(val);
        }

        sb.reverse();
        int start = 0;
        for (; start < sb.length() - 1; start++) {
            if (sb.charAt(start) != '0') {
                break;
            }
        }
        return sb.substring(start);
    }
}
