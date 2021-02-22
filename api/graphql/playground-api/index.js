const express = require("express");
const graphqlHTTP = require("express-graphql");
const bodyparser = require("body-parser");
const { buildSchema } = require("graphql");

const app = express();

app.use(bodyparser.json());

// Setup the route of the API
app.use(
    "/graphql",
    graphqlHTTP({
        // Here we can setup the options for the API
        schema: defineSchema(),
        rootValue: {
            filmography: getMovies()
        },
        graphiql: true
    })
);

app.listen(3232, () => {
    console.log("Server running");
});

function defineSchema() {
    // Define the schema
}

function getMovies() {
    return [
        "Lord of the Rings",
        "Terminator 2",
        "Last Samurai"
    ];
}

