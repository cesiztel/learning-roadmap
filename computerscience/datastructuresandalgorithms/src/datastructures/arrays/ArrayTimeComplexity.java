package datastructures.arrays;

public class ArrayTimeComplexity {

    private int[] myArray;

    public ArrayTimeComplexity()
    {
        initArray();
    }

    /**
     * O(1)
     * No matter who many elements have the array. Get an element
     * with known index only takes one operation.
     */
    public void retrieveWithIndex()
    {
        int index = 4;
        int element = myArray[index];

        System.out.println("retrieveWithIndex = Index: " + index + " with element: " + element);
    }

    /**
     * O(n)
     * The complexity depends on the number of elements.
     *
     * In the worst case, we have to loop over all the array, because the element
     * in the worst case might be in the last position of the array.
     */
    public void retrieveWithOutIndex()
    {
        int elementToFind = 6;
        int indexOfFoundElement = 0;

        for (int i : myArray) {
            if (elementToFind == myArray[i]) {
                indexOfFoundElement = i;
                break;
            }
        }

        System.out.println("retrieveWithOutIndex = Index: " + indexOfFoundElement + " with element: " + elementToFind);
    }

    /**
     * O(n)
     *
     * The only way to redimension an array is to create a brand new array,
     * copy all the elements from the previous one and add the extra
     * element to the end of the new array. The time complexity of copying all
     * the elements from one array to another is dependent to the number
     * of the elements.
     */
    public void addElementToAFullArray()
    {
        int[] newRedimensionedArray = new int[myArray.length + 1];
        int newElement = 15;

        for (int i : myArray)
            newRedimensionedArray[i] = myArray[i];

        newRedimensionedArray[newRedimensionedArray.length - 1] = newElement;

        System.out.println("****** My new Redimensioned array");
        displayArray(newRedimensionedArray);
    }

    /**
     * O(1)
     */
    public void addElementToTheEndOfAnArrayWithSpace()
    {
        myArray[myArray.length - 1] = 13;

        System.out.println("****** Add element to the end of an array with space");
        displayArray(myArray);
        initArray();
    }

    /**
     * O(1)
     */
    public void insertOrUpdateAnElementAtASpecificIndex()
    {
        myArray[myArray.length - 1] = -20;

        System.out.println("****** Insert or update element at specific index");
        displayArray(myArray);
        initArray();
    }

    /**
     * O(1)
     */
    public void deleteAnElementAtASpecificIndex()
    {
        int index = 3;
        myArray[index] = -1;

        System.out.println("****** Delete element at specific index (null or -1)");
        displayArray(myArray);
        initArray();
    }

    /**
     * O(n)
     *
     * Even if the there is a possibility that the index to shift is close
     * to end of the array, so we will loop through the min number of elements.
     * The worst case is that the given index is the first element of the array (0),
     * so we will need to loop through the whole array, shifting elements.
     */
    public void deleteAnElementByShiftingElements()
    {
        int indexToDelete = 3;

        for (int i = indexToDelete; i < myArray.length ; i++) {
            if (i < myArray.length - 1 ) {
                myArray[i] = myArray[i + 1];
            }
            myArray[i] = -1;
        }

        System.out.println("****** Delete element by shifting elements");
        displayArray(myArray);
        initArray();
    }

    private void displayArray(int[] myArray) {
        for (int i : myArray)
            System.out.print(myArray[i] + " ");

        System.out.println();
    }


    private void initArray()
    {
        for(int i=0; i < 10; i++)
            myArray[i] = 2 * i;
    }
}
