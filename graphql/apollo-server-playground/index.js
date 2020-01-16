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
    villian: [Character]!
    allCharacters: [Character]!
  }

  schema {
    query: Query
  }
`;

const resolvers = {
  Query: {
    hero: heroQuery,
    villian: villianQuery,
    allCharacters: allCharactersQuery
  }
};

function heroQuery() {
	return starWarsUniverse.filter(singleCharacter => singleCharacter.hero == true);
}

function villianQuery() {
  return starWarsUniverse.filter(singleCharacter => singleCharacter.hero == false);
}

function allCharactersQuery() {
  return starWarsUniverse;
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
