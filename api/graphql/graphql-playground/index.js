const { ApolloServer, gql } = require("apollo-server");
const { Aletta, Dekker } = require("./aletta");

const schemaDefs = gql`
  enum Level {
    L1_1
    L1_2
    L2_1
    L2_2
    L3_1
    L6
  }

  type PracticeGroup {
    name: String
    lead: ANDI
    members: [ANDI]
  }

  type Squad {
    name: String # Scalar
    lead: ANDI # Object
    members: [ANDI] # List of objects
  }

  type ANDI {
    name: String
    role: String
    ANDtitle: String
    level: Level
  }

  type Query { # Top level entry point for reads
    aletta: [Squad]
    dekker: [Squad]
  }
`;

const resolvers = {
  Level: {
    L1_1: "L1.1",
    L1_2: "L1.2",
    L2_1: "L2.1",
    L2_2: "L2.2",
    L3_1: "L3.1",
    L6: "L6",
  },
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
