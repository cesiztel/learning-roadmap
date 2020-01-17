const { ApolloServer, gql } = require('apollo-server');
const universe = require('./universe');

const starWarsUniverse = universe.buildUniverse();

const typeDefs = gql`
  union Heros = Droid | Jedi

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

  type Jedi implements Character {
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

  input JediInput {
    name: String!
  }

  type Mutation {
    createJedi(input: JediInput!): Jedi
  }

  type Query {
    hero: [Character]!
    villian: [Character]!
    allCharacters: [Character]!
    searchHeros(text: String): [Heros]
  }

  schema {
    query: Query
    mutation: Mutation
  }
`;

const resolvers = {
  Heros: {
    __resolveType(character, context, info){
		  if(character.type == "Jedi") {
			  return 'Jedi';
		  }
	
		  if(character.type == "Droid") {
			  return 'Droid';
		  }
	
		  return null;
		},
  },
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
    allCharacters: allCharactersQuery,
    searchHeros: searchHeros,
  },
  Mutation: {
    createJedi: createJedi
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

function searchHeros(root, args, context) {
  return heroQuery()
    .filter(singleCharacter => singleCharacter.name.toLocaleLowerCase().includes(args.text) == true)
    .filter(singleCharacter => singleCharacter.type != "Human");
}

function createJedi(root, args, context) {
  var newJedi = { 
    name: args.input.name, 
    type: "Jedi", 
    appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
    hero: true
  };

  starWarsUniverse.push(newJedi);

  return newJedi;
}

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
