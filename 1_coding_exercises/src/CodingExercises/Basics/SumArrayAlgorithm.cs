namespace CodingExercises.Basics
{
    public static class SumArrayAlgorithm
    {
        /// <summary>
        /// Take the array [1, 1, 1]
        /// 
        /// [1][1][1] Each element of the array is one integer
        ///  |  |  |
        ///  0  1  2  Because the array is zero index based, the start index is 0 and the final is 2
        ///  
        ///  If we host the array in the variable inputArray and we call to the method inputArray.Length:
        ///  
        ///  inputArray.Length -> 3 (not 2) because is counting the number of elements of the array
        ///  not it's indexes.
        ///  inputArray.Length - 1 => give us the information about which is the top index of the array 
        ///  
        ///  When we try to cross the array we can need to take in account the following:
        ///  for -> loop stopping in the condition
        ///    -> i <= inputArray.Length - 1 => index is less or equal than 3 - 1 (2 the top index)
        ///    -> i <  inputArray.Length     => index is less 3 (so does not loop when reach 3, last element of the loop 2)
        /// 
        /// </summary>
        /// <param name="inputArray"></param>
        /// <returns></returns>
        public static int SumArray(int[] inputArray)
        {
            int totalSum = 0;

            foreach (var element in inputArray)
            {
                totalSum += element;
            }

            return totalSum;
        }

        public static int SumArrayVariation(int[] inputArray)
        {
            int totalSum = 0;

            for (var i = 0; i <= inputArray.Length - 1; i++) // or i < inputArray.Length
            {
                totalSum += inputArray[i];
            }

            return totalSum;
        }
    }
}