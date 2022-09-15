using System;

namespace Delegates
{
    class Program
    {
        public delegate void MyDelegate(int a, int b);
        
        public class OperationalHub
        {
            public event MyDelegate PerformOperationEvent;

            public void FireEvent(int a, int b)
            {
                PerformOperationEvent(a, b);
                Console.WriteLine("Event triggered");
            }
            public void Add(int x, int y)
            {
                Console.WriteLine("Add method {0}", x + y);
            }

            public void Substract(int x, int y)
            {
                Console.WriteLine("Substract method {0}", x - y);
            }
        }

        static void Main(string[] args)
        {
            var calculator = new OperationalHub();
            calculator.PerformOperationEvent += new MyDelegate(calculator.Add);
            calculator.PerformOperationEvent += new MyDelegate(calculator.Substract);
            calculator.FireEvent(10, 5);
        }
    }
}
