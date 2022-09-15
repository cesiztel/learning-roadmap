using System;
using AutoMapper;

namespace AllAboutMapping
{
    class Program
    {
        public class AuthorModel
        {
            public int Id {get; set;}
            public string FirstName {get; set;}
        }

        public class AuthorModelDTO
        {
            public int Id {get; set;}
            public string FirstName {get; set;}
        }

        static void Main(string[] args)
        {
            var config = new MapperConfiguration(config => {
                config.CreateMap<AuthorModel, AuthorModelDTO>();
            });

            IMapper iMapper = config.CreateMapper();
            var source = new AuthorModel {
                Id = 5,
                FirstName = "Cesar"
            };
            var destination = iMapper.Map<AuthorModel, AuthorModelDTO>(source);

            Console.WriteLine("Author name: " + destination.FirstName);
        }
    }
}
