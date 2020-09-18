using System;
using System.ComponentModel.DataAnnotations;

namespace QuotesApi.Models
{
    public class Quote
    {
        public int Id { get; set; }

        //[Required]
        //[StringLength(30)]
        public string Title { get; set; }

        //[Required]
        [StringLength(20)]
        public string Author { get; set; }

        //[Required]
        public string Description { get; set; }

        //[Required]
        public string Type { get; set; }

        public DateTime CreatedAt { get; set; }
    }
}