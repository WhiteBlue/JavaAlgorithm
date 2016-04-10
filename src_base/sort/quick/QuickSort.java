package sort.quick;

/**
 * 快速排序
 */
public class QuickSort {

    public void sort(int[] array, int start, int end) {
        if (start < end) {
            int index = quickSort(array, start, end);
            System.out.println(2);
            sort(array, start, index - 1);
            sort(array, index + 1, end);
        }
    }

    private int quickSort(int[] array, int start, int end) {
        //取末尾元素为主元
        int judge = array[end];

        //标志
        int index = start - 1;
        for (int i = start; i < end; i++) {
            //交换标志元素
            if (array[i] < judge) {
                index++;
                int tmp = array[i];
                array[i] = array[index];
                array[index] = tmp;
            }
        }
        //填最后一个空
        int tmp = array[end];
        array[end] = array[index + 1];
        array[index + 1] = tmp;

        //返回整理过的index
        return index + 1;
    }
}
