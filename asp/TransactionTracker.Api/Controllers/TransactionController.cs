using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace TransactionTracker.Api.Controllers
{
    [ApiController]
    [Route("api/transactions")]
    public class TransactionController : ControllerBase
    {
        private readonly ILogger<TransactionController> _logger;

        public TransactionController(ILogger<TransactionController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IActionResult Index()
        {
            return Ok("List of transactions");
        }

        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            return Ok($"Single transaction with Id: {id}");
        }

        [HttpPost]
        public IActionResult Create()
        {
            return Ok("Transaction created!");
        }

        [HttpPut]
        public IActionResult Update()
        {
            return Ok("Transaction updated");
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            return Ok($"Transaction deleted with Id: {id}");
        }
    }
}