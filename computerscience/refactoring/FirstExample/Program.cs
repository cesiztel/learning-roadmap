using System;
using System.Collections.Generic;

namespace FirstExample
{
    class Program
    {
        static void Main(string[] args)
        {
            var plays = new Dictionary<string, Play>();
            plays.Add("hamlet", new Play {
                Name = "Hamlet",
                Type = "tragedy"
            });
            plays.Add("as-like", new Play {
                Name = "As You Like it",
                Type = "comedy"
            });
            plays.Add("othello", new Play {
                Name = "Othello",
                Type = "tragedy"
            });

            var invoices = new List<Invoice>();
            invoices.Add(new Invoice {
                Customer = "BigCo",
                Performances = new List<Performancer>
                {
                    new Performancer()
                    {
                        PlayerID = "hamlet",
                        Audience = 55
                    },
                    new Performancer()
                    {
                        PlayerID = "as-like",
                        Audience = 35
                    },
                    new Performancer()
                    {
                        PlayerID = "othello",
                        Audience =40
                    }
                }
            });
        }

        private string Statement()
        {

            return string.Empty;
        }
    }

    public class Play
    {
        public string Name { get; set; }

        public string Type { get; set; }
    }

    public class Performancer
    {
        public string PlayerID { get; set; }

        public int Audience { get; set; }
    }

    public class Invoice
    {
        public string Customer { get; set; }

        public List<Performancer> Performances { get; set; }
    }
}
