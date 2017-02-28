import java.util.ArrayList;
import java.util.List;

/**
 * id: 54
 * <p>
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 */
public class SpiralMatrix {

    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0) {
            return new ArrayList<>();
        }
        int x = 0, y = 0, iX = 1, iY = 0, startX = 0, startY = 0, endY = matrix.length - 1, endX = matrix[0].length - 1;
        List<Integer> retArr = new ArrayList<>();

        while (x <= endX && x >= startX && y <= endY && y >= startY) {

            if (x == endX && iX == 1) {
                iX = 0;
                iY = 1;
                startY += 1;
            } else if (y == endY && iY == 1) {
                iX = -1;
                iY = 0;
                endX -= 1;
            } else if (x == startX && iX == -1) {
                iX = 0;
                iY = -1;
                endY -= 1;
            } else if (y == startY && iY == -1) {
                iX = 1;
                iY = 0;
                startX += 1;
            }

            retArr.add(matrix[y][x]);

            x += iX;
            y += iY;

        }

        return retArr;
    }


}
