using System;
using System.Collections.Generic;

namespace PetStore.Models
{
    public class Pet
    {
        public int Id { get; set; }

        public Category Category { get; set; }

        public string Name { get; set; }

        public List<string> PhotoUrls { get; set; }

        public List<Tag> Tags { get; set; }

        public Status Status { get; set; }
    }
}
