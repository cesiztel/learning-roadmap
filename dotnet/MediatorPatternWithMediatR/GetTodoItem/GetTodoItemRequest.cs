using MediatR;

namespace MediatorPatternWithMediatR.GetTodoItem
{
    public class GetTodoItemRequest : BaseRequest, IRequest<Item>
    {
        public int Id { get; set; }
    }
}
