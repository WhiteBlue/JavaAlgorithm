
/**
 * id: 55
 * <p>
 * You are given an n x n 2D matrix representing an image.
 * <p>
 * Rotate the image by 90 degrees (clockwise).
 */

public class RotateImage {

    private void swap(int[][] matrix, int x0, int y0, int x1, int y1) {
        int tmp = matrix[x0][y0];
        matrix[x0][y0] = matrix[x1][y1];
        matrix[x1][y1] = tmp;
    }

    public void rotate(int[][] matrix) {
        int n = matrix.length, start = 0, end = n - 1, deep = 0;
        while (start <= end) {
            start = deep + 1;
            end = n - deep - 2;
            for (int i = start; i <= end; i++) {
                this.swap(matrix, deep, i, i, n - deep - 1);
                this.swap(matrix, i, deep, n - deep - 1, i);
            }
            for (int i = start; i <= end; i++) {
                this.swap(matrix, deep, i, n - deep - 1, end - i + start);
            }
            this.swap(matrix, start - 1, start - 1, start - 1, end + 1);
            this.swap(matrix, end + 1, start - 1, end + 1, end + 1);
            this.swap(matrix, start - 1, start - 1, end + 1, end + 1);
            deep++;
        }
    }


}
