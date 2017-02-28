/**
 * id: 29
 * <p>
 * Divide two integers without using multiplication, division and mod operator.
 * If it is overflow, return MAX_INT.
 */
public class DivideTwoInteger {

    public int divide(int dividend, int divisor) {
        long sum = 0;
        long newDividend = Math.abs((long) dividend);
        long newDivisor = Math.abs((long) divisor);

        while (newDividend >= newDivisor) {
            long innerSum = newDivisor;
            long innerShift = 1;

            while ((innerSum << 1) < newDividend) {
                innerSum <<= 1;
                innerShift <<= 1;
            }

            sum += innerShift;

            newDividend -= innerSum;
        }

        sum = (((dividend ^ divisor) >>> 31) == 0x00000001) ? -sum : sum;

        if (sum > Integer.MAX_VALUE) {
            sum = Integer.MAX_VALUE;
        }
        return (int) sum;
    }


    public static void main(String args[]) {
        DivideTwoInteger d = new DivideTwoInteger();

        System.out.println(d.divide(3455, 1));
    }

}
