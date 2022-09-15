using MediatR;

namespace MediatorPatternWithMediatR
{
    public class Message : INotification
    {
        public string Body { get; set; }
    }
}
