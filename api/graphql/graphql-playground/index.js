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

  union SearchResult = Hub | Club

  type Query { # Top level entry point for reads
    AND: AND
    searchByName(contains: String): [SearchResult]
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
  SearchResult: {
    __resolveType(obj, context, info) {
      if (obj.peoplelead) {
        return "Club";
      }

      return "Hub";
    },
  },
  Query: {
    AND: () => AND,
    searchByName: (parent, args, context, info) => {
      const keyword = args.contains;
      results = [];
      AND.hubs.forEach((hub) => {
        if (hub.name.includes(keyword)) {
          results.push(hub);
        }

        hub.clubs.forEach((club) => {
          if (club.name.includes(keyword)) {
            results.push(club);
          }
        });
      });

      return results;
    },
  },
};

const server = new ApolloServer({
  typeDefs: schemaDefs,
  resolvers: resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
