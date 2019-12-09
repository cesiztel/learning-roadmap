const { ApolloServer, gql } = require('apollo-server');
const { PubSub } = require('apollo-server');

const luke = { name: "Luke Skywalker", type: "Jedi", appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], hero: true };
const han = { name: "Han Solo", type: "Human", appearsIn: ["NEWHOPE", "JEDI"], hero: true };
const r2 = { 
	name: "R2-D2", 
	type: "Droid", 
	appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
	hero: true,
	skills: []
};
const cpo = { 
	name: "C-3PO", 
	type: "Droid", 
	appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
	hero: true,
	skills: ["open dors", "pilor starships"] 
};
const vader = { name: "Darth Vader", type: "Sith", appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], hero: false };

function buildUniverse() {
	luke.father = [vader];
	luke.friends = [han, r2, cpo];
	han.friends = [luke, r2, cpo];
	r2.friends = [han, luke, cpo];
	cpo.friends = [han, luke, r2];
	vader.friends = [];

	return [han, luke, r2, cpo, vader];
}

const starWarsUniverse = buildUniverse();

const pubsub = new PubSub();
// const PARKING_STOPPED = 'PARKING_STOPPED';

const typeDefs = gql`
  enum Episode {
    NEWHOPE
    EMPIRE
    JEDI
  }

  interface Character {
	name: String!
	appearsIn: [Episode!]!
	friends: [Character]
  }

  type Human implements Character {
    name: String!
	appearsIn: [Episode!]!
	friends: [Character]
	age: Int
  }

  type Droid implements Character {
    name: String!
	appearsIn: [Episode!]!
	friends: [Character]
    skills: [String]!
  }

  type Query {
	hero: [Character]
	villian: [Character]
  }
`;

const resolvers = {
    /* Subscription: {
        parkingStopped: {
          subscribe: () => pubsub.asyncIterator([PARKING_STOPPED]),
        },
	}, */
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
		villian: villanQuery
    }
    /* Mutation: {
        stopParkingAction(root, args, context) {
            var stoppedParkingAction = 


            pubsub.publish(PARKING_STOPPED, { parking: args });

            return {
                id: 237613301,
                location: {
                  latitude: "52.340329",
                  longitude: "4.874578",
                  name: "Haarlem - Centrum"
                },
                start: "2019-05-02T13:22:01",
                stop: "2019-05-02T13:24:51",
                type: "OnStreet",
                bill: {
                  price: 0.25,
                  free: 0.27,
                  total: 0.52,
                  currency: {
                    symbol: "€"
                  }
                }
            }
        },
    }, */
};

function heroQuery() {
	return starWarsUniverse.filter(singleCharacter => singleCharacter.hero == true);
}

function villanQuery() {
	return starWarsUniverse.filter(singleCharacter => singleCharacter.hero == false);
}

// The ApolloServer constructor requires two parameters: your schema
// definition and your set of resolvers.
const server = new ApolloServer({ typeDefs, resolvers });

// The `listen` method launches a web server.
server.listen().then(({ url, subscriptionsUrl }) => {
  console.log(`🚀 Server ready at ${url}`);
  console.log(`🚀 Subscriptions ready at ${subscriptionsUrl}`);
});
