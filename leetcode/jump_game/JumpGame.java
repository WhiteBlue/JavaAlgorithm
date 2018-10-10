
/**
 * id: 55
 * <p>
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 * <p>
 * Each element in the array represents your maximum jump length at that position.
 * <p>
 * Determine if you are able to reach the last index.
 */


public class JumpGame {

    public boolean canJump(int[] nums) {
        int tmp = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > tmp) {
                return false;
            }
            tmp = Integer.max(nums[i] + i, tmp);
        }
        return true;
    }

}
