const { ApolloServer, gql } = require("apollo-server");
const { ANDIs } = require("./andis");

const schemaDefs = gql`
  type ANDI {
    name: String
    role: String
    ANDtitle: String
  }

  type Query {
    club: [ANDI]
  }
`;

const resolvers = {
  Query: {
    club: () => ANDIs,
  },
};

const server = new ApolloServer({
  typeDefs: schemaDefs,
  resolvers: resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
