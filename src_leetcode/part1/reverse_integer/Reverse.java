package part1.reverse_integer;

/**
 * id: 7
 * <p>
 * Reverse digits of an integer.
 * <p>
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 */
public class Reverse {

    private static int findIn(int x, int count) {
        double flag = x / Math.pow(10, count);
        if (flag < 1) {
            long back = 0;
            for (int i = count - 1; i >= 0; i--) {
                double pow = Math.pow(10, i);
                double obj = Math.floor(x / pow);
                back += obj * (Math.pow(10, count - i - 1));
                x -= obj * pow;
            }
            if (back < 0 || back > Integer.MAX_VALUE) {
                back = 0;
            }
            return (int) back;
        }
        return findIn(x, count + 1);
    }

    public static int reverse(int x) {
        boolean flag = false;
        if (x < 0) {
            flag = true;
            x = -x;
        }
        int back = findIn(x, 1);
        if (flag) {
            back = -back;
        }
        return back;
    }
}
