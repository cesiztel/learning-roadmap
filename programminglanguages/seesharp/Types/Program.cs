using System;

namespace Types
{
    class Program
    {
        /**
            Those are some of the simple types
         */

        /* Sat = 0 and Sun = 1 ... */
        enum Day { Sat, Sun, Mon, Tue, Wed, Thu, Fri }

        /* Sat = 1 and Sun = 1 ... */
        enum AtypicalDay { Sat = 1, Sun, Mon, Tue, Wed, Thu, Fri }

        public struct Book 
        {
            public decimal price;
            public string title;
            public string author;
        }

        /**
            Reference types
         */
         
        static void Main(string[] args)
        {
            int x = (int)Day.Sun;
            Console.WriteLine("Sun = {0}", x);

            // Atypical Day
            int x1 = (int)AtypicalDay.Sun;
            Console.WriteLine("Sun = {0}", x1);

            var book = new Book()
            {
                price = 32.2m,
                title = "C# for dummies",
                author = "Unknown"
            };
        }
    }
}
