using System;
using Xunit;
using CodingExercises.Basics;

namespace CodingExercises.Test
{
    public class SumArrayTests
    {
        [Fact]
        public void GivenACorrectArrayTheSumIsCorrectTest()
        {
            int expectedSumResult = 5;
            int[] myArray = new int[] {1, 1, 1, 1, 1}; 

            var sumResult = SumArrayAlgorithm.SumArray(myArray);

            Assert.Equal(sumResult, expectedSumResult);
        }

        [Fact]
        public void GivenACorrectArrayTheSumVariationIsCorrectTest()
        {
            int expectedSumResult = 5;
            int[] myArray = new int[] { 1, 1, 1, 1, 1 };
            
            var sumResult = SumArrayAlgorithm.SumArrayVariation(myArray);

            Assert.Equal(sumResult, expectedSumResult);
        }
    }
}
