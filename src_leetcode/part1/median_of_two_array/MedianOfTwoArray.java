package part1.median_of_two_array;

/**
 * id: 4
 * <p>
 * <p>
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 */
public class MedianOfTwoArray {

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        double mid = (double) (nums1.length + nums2.length - 1) / 2;

        //中点的左值和右值
        int left = (int) Math.floor(mid);
        int right = (int) Math.ceil(mid);

        int tmpLeft = 0, tmoRight = 0, count = 0;

        while (count <= right) {
            //初始值设为最大
            int target1 = Integer.MAX_VALUE, target2 = Integer.MAX_VALUE;
            if (i < nums1.length) {
                target1 = nums1[i];
            }
            if (j < nums2.length) {
                target2 = nums2[j];
            }

            //比较两数组取得最小值
            int min;
            if (target1 >= target2) {
                min = target2;
                j++;
            } else {
                min = target1;
                i++;
            }

            //设置左值
            if (count == left) {
                tmpLeft = min;
            }
            tmoRight = min;

            count++;
        }
        //取平均
        return (double) (tmpLeft + tmoRight) / 2;
    }

}
