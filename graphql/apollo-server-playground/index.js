const { ApolloServer, gql } = require('apollo-server');
const universe = require('./universe');

const starWarsUniverse = universe.buildUniverse();

const typeDefs = gql`
  enum Episode {
    NEWHOPE
    EMPIRE
    JEDI
  }

  type Character {
    name: String!
    age: Int
    appearsIn: [Episode]
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
