using System;
using System.Threading;
using System.Threading.Tasks;
using MediatR.Pipeline;

namespace MediatorPatternWithMediatR
{
    public class GenericRequestPostProcessor<TRequest, TResponse> : IRequestPostProcessor<TRequest, TResponse>
    {
        public Task Process(TRequest request, TResponse response, CancellationToken cancellationToken)
        {
            Console.WriteLine(" Finish prepocessing ...");

            return Task.CompletedTask;
        }
    }
}
