const { ApolloServer, gql } = require("apollo-server");
const { Aletta, Dekker } = require("./aletta");

const schemaDefs = gql`
  type Squad {
    name: String # Scalar
    lead: ANDI # Object
    members: [ANDI] # List of objects
  }

  type ANDI {
    name: String
    role: String
    ANDtitle: String
  }

  type Query { # Top level entry point
    aletta: [Squad]
    dekker: [Squad]
  }
`;

const resolvers = {
  Query: {
    aletta: () => Aletta,
    dekker: () => Dekker,
  },
};

const server = new ApolloServer({
  typeDefs: schemaDefs,
  resolvers: resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
