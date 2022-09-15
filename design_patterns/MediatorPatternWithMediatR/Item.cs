namespace MediatorPatternWithMediatR
{
    public class Item
    {
        public int Id { get; set; }

        public string Name { get; set; }

        public bool Finished { get; set; } = false;

        public override string ToString()
        {
            return $"Todo Item: {Id}, {Name} ({(Finished ? "Finished" : "Pending")})";
        }
    }
}
