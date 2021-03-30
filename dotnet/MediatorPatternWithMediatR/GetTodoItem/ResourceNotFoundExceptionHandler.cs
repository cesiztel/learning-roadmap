using System;
using System.Threading;
using System.Threading.Tasks;
using MediatorPatternWithMediatR.Exceptions;
using MediatR.Pipeline;

namespace MediatorPatternWithMediatR.GetTodoItem
{
    public class ResourceNotFoundExceptionHandler : IRequestExceptionHandler<GetTodoItemRequest, Item, ResourceNotFoundException>
    {
        public Task Handle(GetTodoItemRequest request,
            ResourceNotFoundException exception,
            RequestExceptionHandlerState<Item> state,
            CancellationToken cancellationToken)
        {
            Console.WriteLine($" Exception Handler: {typeof(ResourceNotFoundException).FullName}");

            state.SetHandled(new Item());

            return Task.CompletedTask;
        }
    }
}
