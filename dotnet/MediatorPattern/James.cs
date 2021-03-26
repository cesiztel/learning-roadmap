using System;

namespace MediatorPattern
{
    public class James : Collegue
    {
        public James(Mediator mediator) : base(mediator)
        {
        }

        public override void HandleNotification(string message)
        {
            Console.WriteLine(message);
        }
    }
}
