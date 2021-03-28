using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using MediatR;

namespace MediatorPatternWithMediatR.GetTodoItem
{
    public class GetTodoItemHandler : IRequestHandler<GetTodoItemRequest, Item>
    {
        public static List<Item> items = new List<Item>
        {
            new Item { Id = 1, Name = "Go to grocery", Finished = false },
            new Item { Id = 2, Name = "Clean the house", Finished = false }
        };

        public Task<Item> Handle(GetTodoItemRequest request, CancellationToken cancellationToken)
        {
            Item foundItem = null;

            foreach (var item in items)
            {
                if (item.Id == request.Id)
                {
                    foundItem = item;

                    break;
                }
            }

            return Task.FromResult(foundItem);  
        }
    }
}
