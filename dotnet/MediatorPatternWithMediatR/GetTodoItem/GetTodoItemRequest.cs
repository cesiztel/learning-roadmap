using MediatR;

namespace MediatorPatternWithMediatR.GetTodoItem
{
    public class GetTodoItemRequest : IRequest<Item>
    {
        public int Id { get; set; }
    }
}
