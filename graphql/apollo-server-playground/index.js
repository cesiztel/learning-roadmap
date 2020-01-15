const { ApolloServer, gql } = require('apollo-server');
const universe = require('./universe');

const starWarsUniverse = universe.buildUniverse();

const typeDefs = gql`
  type Character {
    name: String!
  }

  type Query {
    hero: [Character]!
  }

  schema {
    query: Query
  }
`;

const resolvers = {
  Query: {
    hero: heroQuery
  }
};

function heroQuery() {
	return starWarsUniverse.filter(singleCharacter => singleCharacter.hero == true);
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
