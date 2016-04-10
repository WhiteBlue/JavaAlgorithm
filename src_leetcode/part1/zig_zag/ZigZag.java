package part1.zig_zag;

/**
 * id : 6
 * <p>
 * <p>
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 * of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 */
public class ZigZag {

    public static String convert(String s, int numRows) {
        char[][] lines = new char[s.length()][numRows];

        int count = 0;
        int line = 0;
        boolean mode = true;
        for (char str : s.toCharArray()) {
            if (count == numRows && mode) {
                //正向到达末尾
                if (numRows > 2) {
                    mode = false;
                    count = numRows - 2;
                } else {
                    count = 0;
                }
                line++;
            } else if (count <= 0 && !mode) {
                //反向到达末尾
                mode = true;
                count = 0;
                line++;
            }
            lines[line][count] = str;

            if (mode) {
                //正向打印
                count++;
            } else {
                //反向打印
                count--;
            }
        }

        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < numRows; i++) {
            for (char[] line1 : lines) {
                if (line1[i] != 0) {
                    stringBuilder.append(line1[i]);
                }
            }
        }
        return stringBuilder.toString();
    }

}
