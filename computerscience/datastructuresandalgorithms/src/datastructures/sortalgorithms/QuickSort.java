package datastructures.sortalgorithms;

/**
 * In-place algorithm
 * Difficult to nail down the time complexity because it will depend on the gap. 
 * Worst case O(n^2) but can perform much better than that.
 * Goal -> reduce the shifting
 * Unstable algorithm
 */
public class QuickSort {
    public static void main(String[] args) {
        int[] intArray = { 20, 35, -15, 7, 55, 1, -22 };
        display(intArray);

        quickSort(intArray, 0, intArray.length);

        display(intArray);
    }

    public static void quickSort(int[] input, int start, int end) {
        if (end - start < 2) {
            return;
        }

        int pivotIndex = partition(input, start, end);
        quickSort(input, start, pivotIndex);
        quickSort(input, pivotIndex + 1, end);
    }

    public static int partition(int[] input, int start, int end) {
        int pivot = input[start];
        int i = start;
        int j = end;

        while (i < j) {
            while (i < j && input[--j] >= pivot);
            if (i < j) {
                input[i] = input[j];
            }

            while (i < j && input[++i] <= pivot);
            if (i < j) {
                input[j] = input[i];
            }
        }

        input[j] = pivot;

        return j;
    }

    public static void display(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }

        System.out.println();
    }
}