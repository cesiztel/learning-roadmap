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
            var sumResult = SumArray.Sum(myArray);

            Assert.Equal(sumResult, expectedSumResult);
        }

        [Fact]
        public void GivenACorrectArrayTheSumVariationIsCorrectTest()
        {
            int expectedSumResult = 5;

            int[] myArray = new int[] { 1, 1, 1, 1, 1 };
            var sumResult = SumArray.SumVariation(myArray);

            Assert.Equal(sumResult, expectedSumResult);
        }
    }
}
