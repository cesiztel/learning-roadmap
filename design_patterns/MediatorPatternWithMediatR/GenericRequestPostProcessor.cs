using System;
using System.Threading;
using System.Threading.Tasks;
using MediatR.Pipeline;

namespace MediatorPatternWithMediatR
{
    public class GenericRequestPreProcessor<TRequest> : IRequestPreProcessor<TRequest>
    {
        public Task Process(TRequest request, CancellationToken cancellationToken)
        {
            Console.WriteLine(" Start prepocessing ...");

            return Task.CompletedTask;
        }
    }
}
