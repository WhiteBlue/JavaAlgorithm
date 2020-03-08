
/**
 * id: 53
 * <p>
 * Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 */

public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int tmp = 0;
        int max = Integer.MIN_VALUE;

        for (int num : nums) {
            tmp += num;
            if (tmp > max) {
                max = tmp;
            }
            if (tmp < 0) {
                tmp = 0;
            }
        }
        return max;
    }

}
