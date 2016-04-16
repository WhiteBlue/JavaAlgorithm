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

    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int newValue = result * 10 + x % 10;
            if (newValue  / 10 != result) {
                return 0;
            }
            result = newValue;
            x = x / 10;
        }

        return result;
    }


    public static void main(String args[]) {
        Reverse reverse = new Reverse();
        int back = reverse.reverse(-233);
        System.out.println(back);
    }
}
