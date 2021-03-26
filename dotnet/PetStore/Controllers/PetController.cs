using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using PetStore.Models;

namespace PetStore.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PetController : ControllerBase
    {
        private static readonly Pet[] Store = new[]
        {
            new Pet {
                Id = 1,
                Category = new Category { Id = 1, Name = "dog" },
                Name = "Doggie",
                PhotoUrls = new List<string> { "picture1" },
                Tags = new List<Tag> { new Tag { Id = 1, Name = "canis" } },
                Status = Status.AVAILABLE
            }
        };

        private readonly ILogger<PetController> _logger;

        public PetController(ILogger<PetController> logger)
        {
            _logger = logger;
        }

        [HttpGet("{id}")]
        public ActionResult<Pet> Get(int id)
        {
            foreach (var pet in Store)
            {
                if (pet.Id == id)
                {
                    return pet;
                }
            }

            return NotFound();
        }
    }
}
