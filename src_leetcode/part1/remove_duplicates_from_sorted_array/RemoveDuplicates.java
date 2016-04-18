package part1.remove_duplicates_from_sorted_array;

/**
 * id: 26
 * <p>
 * Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
 * Do not allocate extra space for another array, you must do this in place with constant memory.
 */
public class RemoveDuplicates {

    /**
     * 循环求解,O(n)
     *
     * @param nums array
     * @return result
     */
    public int removeDuplicates(int[] nums) {
        int i = 1;

        for (int j = 1; j < nums.length; j++) {
            if (nums[j - 1] != nums[j]) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}
