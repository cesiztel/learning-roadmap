using System;
using System.Threading;

namespace ThreadFields
{
    class Program
    {
        [ThreadStatic]
        /*
           With Thread static the variable is copied to
           both threads so each thread will keep a copy
           of the variable with out affecting each other. 

           Use Thread.CurrentThread to get thread info.
        */
        public static int _field;

        static void Main(string[] args)
        {
            new Thread(() => 
            {
                for(int x = 0; x < 10; x++)
                {
                    _field++;
                    Console.WriteLine("Thread A: {0}", _field);
                }
            }).Start();

            new Thread(() => 
            {
                for(int x = 0; x < 10; x++)
                {
                    _field++;
                    Console.WriteLine("Thread B: {0}", _field);
                }
            }).Start();

            Console.ReadKey();
        }
    }
}
