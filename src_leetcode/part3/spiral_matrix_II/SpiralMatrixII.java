/**
 * id: 59
 * <p>
 * Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
 */

public class SpiralMatrixII {

    public int[][] generateMatrix(int n) {
        //prepare arr
        int[][] matrix = new int[n][n];
        //prepare var
        int x_start = 0, x_end = n - 1, y_start = 0, y_end = n - 1;

        int i = 1;
        while (x_start <= x_end && y_start <= y_end) {
            for (int a = x_start; a <= x_end; a++) {
                matrix[y_start][a] = i;
                i++;
            }
            y_start++;
            for (int b = y_start; b <= y_end; b++) {
                matrix[b][x_end] = i;
                i++;
            }
            x_end--;
            for (int c = x_end; c >= x_start; c--) {
                matrix[y_end][c] = i;
                i++;
            }
            y_end--;
            for (int d = y_end; d >= y_start; d--) {
                matrix[d][x_start] = i;
                i++;
            }
            x_start++;
        }
        return matrix;
    }

}
