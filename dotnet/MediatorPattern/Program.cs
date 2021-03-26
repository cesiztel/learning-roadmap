namespace MediatorPattern
{
    class Program
    {
        static void Main(string[] args)
        {
            var mediator = new MediatorBen();
            var jon = new Jon(mediator);
            var james = new James(mediator);
            mediator.Jon = jon;
            mediator.James = james;

            jon.Send("Hi James. How are you doing?");
            james.Send("Hi m***f**r. How is possible that we love the same girl?");
        }
    }
}
