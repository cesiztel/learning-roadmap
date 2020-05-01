using System;
using System.Collections.Generic;

namespace DoSomeReflection
{
    class Program
    {
        class Bar 
        {
            public string A {get; set;}
        }

        class Foo 
        {
            public int A {get;set;}

            public string B {get;set;}

            public float C {get;set;}

            public bool D {get; set;}

            public Bar Bar {get; set;}

            public List<string> E {get; set;}
        }

        static void Main(string[] args)
        {
            Foo foo = new Foo 
            {
                A = 1, 
                B = "abc",
                C = 2.5f,
                D = true,
                Bar = new Bar {
                    A = "hello"
                },
                E = new List<string> { "hello", "there" }
            };

            foreach(var prop in foo.GetType().GetProperties()) {
                Console.WriteLine("[{0}]{1}={2}", prop.PropertyType.Name, prop.Name, prop.GetValue(foo, null));
                Console.WriteLine( prop.PropertyType.IsGenericType);
            }
        }
    }
}
