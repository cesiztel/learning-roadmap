package datastructures;

/**
 * In-place algorithm
 * Difficult to nail down the time complexity because it will depend on the gap. 
 * Worst case O(n^2) but can perform much better than that.
 * Goal -> reduce the shifting
 * Unstable algorithm
 */
public class Factorial {
    public static void main(String[] args) {
        
    }

    // 1! =             1 = 1 * 0!
    // 2! =         2 * 1 = 2 * 1!
    // 3! =     3 * 2 * 1 = 3 * 2!
    // 4! = 4 * 3 * 2 * 1 = 4 * 3!

    // n! = n * (n - 1)!
    public static int iterativeFactorial(int num) {
        if (num == 0)
            return 1;
        
        int factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        return factorial;
    }

    public static int recursiveFactorial(int num) {
        if (num == 0)
            return 1;
        
        return num * recursiveFactorial(num - 1);
    }
}