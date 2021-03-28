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
                .BuildServiceProvider();

            var mediator = serviceProvider.GetService<IMediator>();

            // Mediator send request to handler
            var response = mediator.Send(new GetTodoItemRequest { Id = 1 });

            if (response.Result == null)
            {
                Console.WriteLine("No items found");
            }
            else
            {
                Console.WriteLine(response.Result.ToString());
            }

            // Mediator spread the message to other objects
            mediator.Publish(new Message { Body = "Tonight we go to the cinema." });
        }
    }
}
