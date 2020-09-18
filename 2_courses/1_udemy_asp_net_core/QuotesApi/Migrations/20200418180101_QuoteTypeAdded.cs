using Microsoft.EntityFrameworkCore.Migrations;

namespace QuotesApi.Migrations
{
    public partial class QuoteTypeAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Type",
                table: "Quotes",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Type",
                table: "Quotes");
        }
    }
}
