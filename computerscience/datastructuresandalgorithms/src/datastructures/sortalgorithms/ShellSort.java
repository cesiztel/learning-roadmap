package datastructures.sortalgorithms;

/**
 * In-place algorithm
 * Difficult to nail down the time complexity because it will depend on the gap. 
 * Worst case O(n^2) but can perform much better than that.
 * Goal -> reduce the shifting
 * Unstable algorithm
 */
public class ShellSort {
    public static void main(String[] args) {
        int[] intArray = { 20, 35, -15, 7, 55, 1, -22 };
        display(intArray);

        for (int gap = intArray.length / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < intArray.length; i++) {
                int newElement = intArray[i];
                int j = i;

                while (j >= gap && intArray[j - gap] > newElement) {
                    intArray[j] = intArray[j - gap];
                    j -= gap;
                }

                intArray[j] = newElement;

                display(intArray);
            }
        }
    }

    public static void display(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }

        System.out.println();
    }
}