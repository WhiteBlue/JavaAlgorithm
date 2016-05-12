package part2.search_for_a_range;

/**
 * id: 34
 * <p>
 * Given a sorted array of integers, find the starting and ending position of a given target value.
 * <p>
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * <p>
 * If the target is not found in the array, return [-1, -1].
 */
public class SearchForRange {

    private int[] search(int[] nums, int target, int start, int end) {
        if (start > end) {
            return new int[]{-1, -1};
        }
        int mid = (start + end) / 2;
        if (nums[mid] > target) {
            return search(nums, target, start, mid - 1);
        } else if (nums[mid] == target) {
            int i = mid - 1, j = mid + 1;
            while (i >= 0 && nums[i] == target) {
                i--;
            }
            while (j < nums.length && nums[j] == target) {
                j++;
            }
            return new int[]{i + 1, j - 1};
        } else {
            return search(nums, target, mid + 1, end);
        }
    }

    public int[] searchRange(int[] nums, int target) {
        return search(nums, target, 0, nums.length - 1);
    }


    public static void main(String args[]) {

        SearchForRange searchForRange = new SearchForRange();

        int[] nums = new int[]{1};

        int[] back = searchForRange.searchRange(nums, 1);

        System.out.println(back);

    }

}
