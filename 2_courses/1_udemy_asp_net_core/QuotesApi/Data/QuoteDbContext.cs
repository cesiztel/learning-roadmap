using Microsoft.EntityFrameworkCore;
using QuotesApi.Models;

namespace QuotesApi.Data
{
    public class QuotesDbContext : DbContext
    {
        public DbSet<Quote> Quotes { get; set; }

        public QuotesDbContext(DbContextOptions<QuotesDbContext>options): base(options)
        {
        }
    }
}