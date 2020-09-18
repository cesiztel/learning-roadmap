using System;
using System.Collections.Generic;
using System.Linq;
using ExpressoApi.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;

namespace ExpressoApi.Data
{
    public class DataGenerator
    {
        public static void Initialize(IServiceProvider serviceProvider)
        {
            using (var context = new ExpressoDbContext(
                serviceProvider.GetRequiredService<DbContextOptions<ExpressoDbContext>>()
            ))
            {
                if (context.Menus.Any())
                {
                    return; // Data was already seeded
                }

                context.Menus.AddRange(
                    new Models.Menu
                    {
                        Id = 1,
                        Name = "Coffee",
                        Image = "https://i.imgur.com/X586Cvc.jpeg",
                        SubMenus = new List<SubMenu>()
                        {
                            new SubMenu()
                            {
                                Id = 1,
                                Name = "Capuccino",
                                Description = "A capuccino is an espresso-based ...",
                                Price = 10,
                                Image = ""
                            }
                        }
                    },
                    new Models.Menu
                    {
                        Id = 2,
                        Name = "Tea",
                        Image = ""
                    },
                    new Models.Menu
                    {
                        Id = 3,
                        Name = "Cold Drinks",
                        Image = ""
                    }
                );

                context.SaveChanges();
            }
        }
    }
}