using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ExpressoApi.Data;
using ExpressoApi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace ExpressoApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ReservationController : ControllerBase
    {
        ExpressoDbContext _expressoDbContext;

        public ReservationController(ExpressoDbContext expressoDbContext)
        {
            _expressoDbContext = expressoDbContext;
        }

        [HttpPost]
        public IActionResult Post(Reservation reservation)
        {
            _expressoDbContext.Reservations.Add(reservation);
            _expressoDbContext.SaveChanges();

            return StatusCode(StatusCodes.Status201Created);
        }
    }
}
