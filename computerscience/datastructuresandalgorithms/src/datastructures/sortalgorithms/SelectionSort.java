package datastructures.sortalgorithms;

/**
 * In-place algorithm
 * O(n^2)
 * !! unstable algorithm
 */
public class SelectionSort {

    public static void main(String[] args) {
        int[] intArray = { 20, 35, -15, 7, 55, 1, -22 };
        display(intArray);
        
        for (int lastUnsortedIndex = intArray.length - 1; lastUnsortedIndex > 0; lastUnsortedIndex--) {
            int largest = 0;
            for (int i = 1; i <= lastUnsortedIndex ; i++) {
                if (intArray[i] > intArray[largest]) {
                    largest = i;
                }
            }

            swap(intArray, largest, lastUnsortedIndex);

            display(intArray);
        }
    }

    public static void display(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }

        System.out.println();
    }

    public static void swap(int[] array, int i, int j) {
        if (i == j) 
            return;
        
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}