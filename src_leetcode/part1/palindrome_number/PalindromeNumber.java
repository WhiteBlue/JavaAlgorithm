package part1.palindrome_number;

/**
 * id: 9
 * <p>
 * Determine whether an integer is a palindrome. Do this without extra space.
 */
public class PalindromeNumber {


    /**
     * 黑科技解法
     *
     * @param x input
     * @return boolean
     */
    public static boolean isPalindrome(int x) {
        if (x >= 0 && x < 10) {
            return true;
        }

        if (x < 0 || x % 10 == 0) {
            return false;
        }

        //反转目标
        int reverse = 0;
        while (x > reverse) {
            //reverse左移位并加上x最低位
            reverse = reverse * 10 + x % 10;
            //x右移位
            x = x / 10;
        }


        //刚好相等(位数2n)或者对称(位数2n+1)
        return (x == reverse) || (x == reverse / 10);
    }

}
