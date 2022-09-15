namespace MediatorPattern
{
    public abstract class Collegue
    {
        protected Mediator _mediator;

        public Collegue(Mediator mediator)
        {
            _mediator = mediator;
        }

        public virtual void Send(string message)
        {
            _mediator.Say(message, this);
        }

        public abstract void HandleNotification(string message);
    }
}