using System;
using MediatorPatternWithMediatR.GetTodoItem;
using MediatR;
using Microsoft.Extensions.DependencyInjection;

namespace MediatorPatternWithMediatR
{
    class Program
    {
        static void Main(string[] args)
        {
            var serviceProvider = new ServiceCollection()
                .AddMediatR(typeof(Program))
                .AddTransient(typeof(IPipelineBehavior<,>), typeof(SourceLoggingBehavior<,>))
                .BuildServiceProvider();

            var mediator = serviceProvider.GetService<IMediator>();

            // Mediator send request to handler
            var response = mediator.Send(new GetTodoItemRequest { Id = -1, Source = "Android" }); // put -1 to throw an exception

            Console.WriteLine(response.Result.ToString());

            // Mediator spread the message to other objects
            mediator.Publish(new Message { Body = "Tonight we go to the cinema." });
        }
    }
}
