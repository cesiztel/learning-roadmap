package datastructures.arrays;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] intArray = new int[10];

        // Allocate and initialize array
        for (int i = 0; i < 10; i++)
            intArray[i] = - 3 * i;

        // Display, sort, and display the array
        System.out.print("Original contents: ");
        display(intArray);

        Arrays.sort(intArray); // Perform sorting over the same array

        System.out.print("Sorted: ");
        display(intArray);

        // Fill and display the array
        Arrays.fill(intArray, 2, 6, -1);
        System.out.print("After fill(): ");
        display(intArray);

        // Sort and display the array
        Arrays.sort(intArray);
        System.out.print("After sorting again:");
        display(intArray);

        // Binary search
        System.out.print("The value -9 is at location ");
        int index = Arrays.binarySearch(intArray, -9);

        System.out.println(index);
    }

    public static void display(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }

        System.out.println();
    }
}
