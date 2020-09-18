using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ExpressoApi.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace ExpressoApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MenuController : ControllerBase
    {
        ExpressoDbContext _expressoDbContext;

        public MenuController(ExpressoDbContext expressoDbContext)
        {
            _expressoDbContext = expressoDbContext;
        }

        [HttpGet]
        public IActionResult GetMenus()
        {
            var menus = _expressoDbContext.Menus.Include("SubMenus");

            return Ok(menus);
        }

        [HttpGet("{id}")]
        public IActionResult GetMenu(int id)
        {
            var menu = _expressoDbContext.Menus.Include("SubMenus")
                .FirstOrDefault(m => m.Id == id);
            if (menu == null)
            {
                return NotFound();
            }

            return Ok(menu);
        }
    }
}
