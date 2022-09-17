const { ApolloServer, gql } = require("apollo-server");
const { ANDIs, AND } = require("./and");

const schemaDefs = gql`
  enum Level {
    L1_1
    L1_2
    L2_1
    L2_2
    L3_1
    L5_1
    L6
  }

  type AND {
    ceo: ANDI
    hubs: [Hub]
  }

  type Hub {
    name: String
    executive: ANDI
    clubs: [Club]
  }

  type Club {
    name: String
    executive: ANDI
    peoplelead: ANDI
    squads: [Squad]
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
    AND: AND
  }
`;

const resolvers = {
  Level: {
    L1_1: "L1.1",
    L1_2: "L1.2",
    L2_1: "L2.1",
    L2_2: "L2.2",
    L3_1: "L3.1",
    L5_1: "L5.1",
    L6: "L6",
  },
  Query: {
    AND: () => AND,
  },
};

const server = new ApolloServer({
  typeDefs: schemaDefs,
  resolvers: resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
