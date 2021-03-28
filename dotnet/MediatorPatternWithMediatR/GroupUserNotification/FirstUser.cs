using System;
using System.Threading;
using System.Threading.Tasks;
using MediatR;

namespace MediatorPatternWithMediatR.GroupUserNotification
{
    public class FirstUser : INotificationHandler<Message>
    {
        public Task Handle(Message notification, CancellationToken cancellationToken)
        {
            Console.WriteLine($"First user received: {notification.Body}");

            return Task.CompletedTask;
        }
    }
}
