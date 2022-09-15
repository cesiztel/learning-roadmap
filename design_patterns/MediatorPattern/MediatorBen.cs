namespace MediatorPattern
{
    public class MediatorBen : Mediator
    {
        public Jon Jon { get; set; }

        public James James { get; set; }

        public override void Say(string message, Collegue collegue)
        {
            if (collegue == Jon)
            {
                James.HandleNotification(message);
            }
            else 
            {
                Jon.HandleNotification(message);
            }
        }
    }
}
