using System;

namespace CustomMappingSystem
{
    // Reference: https://www.codeproject.com/Tips/781202/Csharp-Custom-Mapper

    public class User 
    {
        public string Name { get; set; }
        public string Address { get; set; }
    }

    public class UserDto
    {
        public string UserName { get; set; }
        public string UserAddress { get; set; }
    }

    public abstract class MapperBase<TFirst, TSecond>
    {
        public abstract TFirst Map(TSecond element);
        public abstract TSecond Map(TFirst element);
    }

    public sealed class UserMapper : MapperBase<User, UserDto>
    {
        public override User Map(UserDto element)
        {
            return new User
            {
                Name = element.UserName,
                Address = element.UserAddress
            };
        }

        public override UserDto Map(User element)
        {
            return new UserDto
            {
                UserName = element.Name,
                UserAddress = element.Address
            };
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var userMapper = new UserMapper();
            var userDto = userMapper.Map(new User {
                Name = "cesiztel",
                Address = "cloud"
            });
            Console.WriteLine("User name => " + userDto.UserName);
            Console.WriteLine("User address => " + userDto.UserAddress);
        }
    }
}
