package part1.two_sum;

public class Two_sum {

    public static int[] twoSum(int[] nums, int target) {
        for (int a = 0; a < nums.length; a++) {
            for (int b = a + 1; b < nums.length; b++) {
                if ((nums[a] + nums[b]) == target) {
                    return new int[]{a, b};
                }
            }
        }
        return new int[]{};
    }
}
