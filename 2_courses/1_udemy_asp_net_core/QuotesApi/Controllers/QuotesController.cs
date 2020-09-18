using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using QuotesApi.Data;
using QuotesApi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Authorization;
using System.Security.Claims;

namespace QuotesApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    //[Authorize]
    public class QuotesController : ControllerBase
    {
        private QuotesDbContext _quotesDbContext;

        public QuotesController(QuotesDbContext quotesDbContext)
        {
            _quotesDbContext = quotesDbContext;
        }
        
        [HttpGet]
        // Any -> save cache in client and proxy server
        // Client
        // None -> by default Any
        [ResponseCache(Duration = 60, Location = ResponseCacheLocation.Any)]
        public IActionResult Get(string type, string sort = "desc")
        {
            // IEnumerable<Quote> es menos eficiente por que el ORM pasa
            // todos los rows a la variable en memoria y despues
            // haras la query.
            // IQueryable solo devolvera los rows que se hayan 
            // hecho la query directamente
            // En este caso IEnumerable haria:
            // 1. select * from quotes; -> devolviendolo a la variable quotes
            // 2. quotes orderby createdAt
            // En IQueryable haria:
            // 1. select * from quotes orderby createdAt -> devolviendo esto a quotes
            IQueryable<Quote> quotes;
            
            quotes = (type != null) ?
                _quotesDbContext.Quotes.Where(q => q.Type.StartsWith(type)) :
                _quotesDbContext.Quotes;

            quotes = (sort == "asc") ? 
                quotes.OrderBy(q => q.CreatedAt) :
                quotes.OrderByDescending(q => q.CreatedAt);

            return Ok(quotes);
        }

        [HttpGet("[action]")]
        public IActionResult PagingQuote(int page = 1, int pageSize = 5)
        {
            var quotes = _quotesDbContext.Quotes;

            // 1 - 1 * 5 => skip(0).Take(5) -> (x - 1) * n -> rango n elmentos
            // 2 - 1 * 5 => skip(5).Take(5)
            return Ok(quotes.Skip((page-1)*pageSize).Take(pageSize));
        }

        [HttpGet("{id}", Name = "Get")]
        public IActionResult Get(int id)
        {
            var quote = _quotesDbContext.Quotes.Find(id);

            if (quote == null)
            {
                return NotFound();
            }

            return Ok(quote);
        }

        [HttpPost]
        public IActionResult Post([FromBody]Quote quote)
        {
            // podremos saber el usuario logado en ese momento.
            //var userId = User.Claims.FirstOrDefault(c => c.Type == ClaimTypes.NameIdentifier).Value;

            _quotesDbContext.Quotes.Add(quote);

            _quotesDbContext.SaveChanges();

            return StatusCode(StatusCodes.Status201Created);
        }

        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody]Quote newQuote)
        {
            var quote = _quotesDbContext.Quotes.Find(id);
            if (quote == null)
            {
                return NotFound();
            }

            quote.Title = newQuote.Title;
            quote.Description = newQuote.Description;
            quote.Author = newQuote.Author;
            quote.Type = newQuote.Type;
            quote.CreatedAt = newQuote.CreatedAt;

            _quotesDbContext.SaveChanges();

            return Ok();
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var quote = _quotesDbContext.Quotes.Find(id);
            if (quote == null)
            {
                return NotFound();
            }

            _quotesDbContext.Remove(quote);
            _quotesDbContext.SaveChanges();

            return Ok();
        }   
    }
}
