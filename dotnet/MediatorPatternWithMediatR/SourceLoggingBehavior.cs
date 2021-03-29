using System;
using System.Threading;
using System.Threading.Tasks;
using MediatR;

namespace MediatorPatternWithMediatR
{
    public class SourceLoggingBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
    {
        public async Task<TResponse> Handle(TRequest request, CancellationToken cancellationToken, RequestHandlerDelegate<TResponse> next)
        {
            if (request is BaseRequest)
            {
                var todoItemRequest = (BaseRequest)(object)request;

                Console.WriteLine($"Request source: {todoItemRequest.Source}");
            }

            var response = await next();

            return response;
        }
    }
}
