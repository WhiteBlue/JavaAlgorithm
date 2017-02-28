/**
 * id: 35
 * <p>
 * Given a sorted array and a target value, return the index if the target is found.
 * If not, return the index where it would be if it were inserted in order.
 */
public class SearchInsertPosition {


    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        int ret = (start + end) / 2;
        ret = nums[ret] > target ? ret - 1 : ret + 1;

        return ret < 0 ? 0 : ret;
    }


}
