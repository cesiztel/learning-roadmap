using System;
using System.Collections.Generic;

namespace IsAboutGenerics
{
    /// <summary>
    /// Coding exercise with generics:
    /// 1. Copying lists. Given one list of any type, copy to another list
    /// 2. Copying first range. Given one list of any type, copy a range of elements
    ///    starting for the begining of the list
    /// 3. Copying range. Given one list of any type and a bound window, copy the range
    ///    of elements of that window
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            var originalList1 = new List<string>() { "BMW", "Mercedes-Benz", "Toyota" };
            var originalList2 = new List<int>() { 1, 1, 2, 3, 5, 8, 13, 21 };

            Console.WriteLine("Original list -> originalList1");
            Display(originalList1);
            
            var arrayCopy = CopyAtMost<string>(originalList1);
            
            Console.WriteLine("Copy done ... ");
            Display(arrayCopy);

            Console.WriteLine("Original list -> originalList1");
            Display(originalList1);

            Console.WriteLine("Coping first 2 elements");
            Display(originalList1);

            var listFirstCopy = CopyFirst<string>(originalList1, 2);

            Console.WriteLine("Copy done ... ");
            Display(listFirstCopy);
        }

        public static List<T> CopyFirst<T>(List<T> inputList, int elementsToCopy)
        {
            var newList = new List<T>();

            int maxCopy = Math.Min(elementsToCopy, inputList.Count);
            
            if (maxCopy == 0)
            {
                return newList;
            }
             
            for (var i = 0; i < maxCopy; i++)
            {
                newList.Add(inputList[i]);    
            }

            return newList;
        }

        public static List<T> CopyAtMost<T>(List<T> inputList)
        {
            var newList = new List<T>();

            for (var i = 0; i < inputList.Count; i++)
            {
                newList.Add(inputList[i]);    
            }

            return newList;
        }

        public static void Display<T>(List<T> inputList)
        {
            for (var i = 0; i < inputList.Count; i++)
            {
                Console.WriteLine($"Position {i}, Value {inputList[i]}");
            }
        }
    }
}
