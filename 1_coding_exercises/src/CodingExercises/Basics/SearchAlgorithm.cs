namespace CodingExercises.Basics
{
    public static class SearchAlgorithm
    {
        /// <summary>
        /// Conceptually we can reason that if the element is not in the array
        /// this algorithm will have to transverse all the array in order 
        /// to determine that the element is not in the array and should return
        /// -1 (worst scenario)
        /// 
        /// As quickest scenario, the search element is in the first position of the 
        /// array (best scenario)
        /// Also we can deduct that as bigger the array is, the lowest is the algorithm
        /// to find the element, because at the end the base idea is tranverse the
        /// whole array, independently of the size. 
        /// </summary>
        /// <param name="arr"></param>
        /// <param name="value"></param>
        /// <returns></returns>
        public static int SequentialSearch(int[] arr, int value)
        {
            for (var i = 0; i < arr.Length; i++)
            {
                if (arr[i] == value)
                {
                    return arr[i];
                }
            }

            return -1;
        }

        /// <summary>
        /// Sequential Seach can work with order and unorder algorithms, but
        /// if you know in front that your array is going to be ordered, there
        /// is an algorithm which is quicker that the SequentialSearch.
        /// 
        /// </summary>
        /// <param name="inputArray"></param>
        /// <returns></returns>
        public static int BinarySeach(int[] arr, int value)
        {
            return 0;
        }
    }
}