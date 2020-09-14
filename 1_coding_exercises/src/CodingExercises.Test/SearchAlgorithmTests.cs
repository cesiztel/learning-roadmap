using System;
using Xunit;
using CodingExercises.Basics;

namespace CodingExercises.Test
{
    public class SearchAlgorithmTests
    {
        [Fact]
        public void GivenAValueInTheArrayReturnsTheValue()
        {
            int searchValue, expectedFoundValue;
            searchValue = expectedFoundValue = 5;
            int[] myArray = new int[] {1, 2, 3, 4, 5}; 

            var foundValue = SearchAlgorithm.SequentialSearch(myArray, searchValue);

            Assert.Equal(foundValue, expectedFoundValue);
        }

        [Fact]
        public void GivenAValueNotPresentInTheArrayReturnsMinusOne()
        {
            int searchValue, expectedFoundValue;
            searchValue = 5;
            expectedFoundValue = -1;
            int[] myArray = new int[] { 1, 1, 1, 1, 1 };
            
            var foundValue = SearchAlgorithm.SequentialSearch(myArray, searchValue);

            Assert.Equal(foundValue, expectedFoundValue);
        }
    }
}
