package part1.container_with_max_ater;

/**
 * id: 11
 * <p>
 * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 * Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 */
public class ContainerWithMaxWater {

    /**
     * O(n^2)
     *
     * @param height array
     * @return int
     */
    public int maxAreaPoor(int[] height) {
        int len = height.length;
        int[][] cache = new int[len][len];
        int max = 0;
        for (int a = 0; a < len; a++) {
            for (int b = a + 1; b < len; b++) {
                int full = (b - a) * Math.min(height[a], height[b]);
                if (full > max) {
                    max = full;
                }
            }
        }
        return max;
    }

    /**
     * O(n),黑科技
     *
     * @param height array
     * @return int
     */
    public int maxArea(int[] height) {
        int i = 0, j = height.length - 1;
        int max = 0;
        while (i < j) {
            int result = (j - i) * Math.min(height[i], height[j]);
            if (result > max) {
                max = result;
            }
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return max;
    }

}
