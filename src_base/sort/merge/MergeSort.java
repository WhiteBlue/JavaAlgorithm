package sort.merge;

/**
 * 归并排序
 */
public class MergeSort {

    public int[] sort(int[] list, int start, int end) {
        if (start == end) {
            return new int[]{};
        }
        int mid = (start + end) / 2;
        return merge(sort(list, start, mid), sort(list, mid + 1, end));
    }

    private int[] merge(int[] listA, int[] listB) {
        int[] result = new int[listA.length + listB.length];
        int i = 0, j = 0, index = 0;
        while (i < listA.length && j < listB.length) {
            int targetA = listA[i];
            int targetB = listB[j];
            if (targetA > targetB) {
                result[index] = targetB;
                j++;
            } else {
                result[index] = targetA;
                i++;
            }
            index++;
        }

        for (; i < listA.length; i++) {
            result[index] = listA[i];
            index++;
        }
        for (; j < listB.length; j++) {
            result[index] = listA[j];
            index++;
        }

        return result;
    }
}
