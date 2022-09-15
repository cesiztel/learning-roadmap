using System;

namespace MediatorPattern
{
    public class Jon : Collegue
    {
        public Jon(Mediator mediator) : base(mediator)
        {
        }

        public override void HandleNotification(string message)
        {
            Console.WriteLine(message);
        }
    }
}
