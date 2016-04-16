package others;

/**
 * 蛇形打印数组
 */
public class PrintArrayRound {

    public void print(int n) {
        int[][] list = new int[n][n];

        int count = 1;
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int i = n - 1, j = 0;
        for (int flag = 0; flag < Math.ceil(n / 2); flag++) {
            //右上对齐
            while (j <= bottom) {
                list[i][j++] = count++;
            }
            i--;
            j--;
            right--;
            //右下对齐
            while (i >= left) {
                list[i--][j] = count++;
            }
            i++;
            j--;
            bottom--;
            //左下对齐
            while (j >= top) {
                list[i][j--] = count++;
            }
            j++;
            i++;
            left++;
            //左上对齐
            while (i <= right) {
                list[i++][j] = count++;
            }
            i--;
            j++;
            top++;
        }

        //打印结果
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                System.out.print(list[j][i] + " ");
            }
            System.out.print("\n");
        }
    }
}


