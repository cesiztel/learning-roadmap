const { ApolloServer, gql } = require('apollo-server');
const universe = require('./universe');

const starWarsUniverse = universe.buildUniverse();

const typeDefs = gql`
  enum Episode {
    NEWHOPE
    EMPIRE
    JEDI
  }

  interface Character {
    name: String!
    age: Int
    appearsIn: [Episode]
    friends: [Character]
  }

  type Human implements Character {
    name: String!
    age: Int
    appearsIn: [Episode]
    friends: [Character]
  }
  
  type Droid implements Character {
    name: String!
    age: Int
    appearsIn: [Episode]
    friends: [Character]
    skills: [String]!
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
  Character: {
    __resolveType(character, context, info){
		  if(character.type == "Human" || character.type == "Jedi" || character.type == "Sith") {
			  return 'Human';
		  }
	
		  if(character.type == "Droid") {
			  return 'Droid';
		  }
	
		  return null;
		},
  },
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
