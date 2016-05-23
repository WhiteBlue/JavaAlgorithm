package sort.heap;

/**
 * 堆排序
 */
public class HeapSort {

    private void minHeap(int[] array, int i) {
        //父节点
        int j = 2 * i + 1;
        int tmp;

        while (j < array.length) {
            tmp = array[i];
            //左右中找最小
            if (j + 1 < array.length && array[j + 1] < array[j]) {
                j++;
            }
            //父节点大于子节点
            if (array[j] < tmp) {
                int swap = array[j];
                array[j] = array[i];
                array[i] = swap;
                //继续浮动
                i = j;
            } else {
                break;
            }
        }
    }


    private void buildHeap(int[] array) {
        for (int i = array.length - 1; i >= 0; i--) {
            minHeap(array, i);
        }
    }

    public static void main(String args[]) {
        HeapSort h = new HeapSort();

        int[] target = {5, 7, 9, 4, 6, 3, 2};

        h.buildHeap(target);

        for (int i : target) {
            System.out.println(i);
        }
    }

}

