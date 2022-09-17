const { ApolloServer, gql } = require("apollo-server");
const { ANDIs, AND, books } = require("./and");
const { GraphQLScalarType, Kind, parseValue } = require("graphql");

const dateScalar = new GraphQLScalarType({
  name: "Date",
  description: "Date custom scalar type",
  serialize(value) {
    return value.getTime(); // Convert outgoing Date to integer for JSON
  },
  parseValue(value) {
    return new Date(value); // Convert incoming integer to Date
  },
  parseLiteral(ast) {
    if (ast.kind === Kind.INT) {
      return new Date(parseInt(ast.value, 10)); // Convert hard-coded AST string to integer and then Date
    }
    return null; // Invalid hard-coded value (not an integer)
  },
});

const schemaDefs = gql`
  scalar Date

  interface Book {
    title: String!
    author: Author! @deprecated(reason: "Use 'newField'.")
    date: Date!
  }

  type Author {
    name: String
  }

  type Course {
    name: String
  }

  type Textbook implements Book {
    title: String!
    author: Author!
    date: Date!
    courses: [Course!]!
  }

  type ColoringBook implements Book {
    title: String!
    author: Author!
    date: Date!
    colors: [String!]!
  }

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

  fragment UnitDetails on Hub {
    name: String
    executive: ANDI
  }

  input ClubInput {
    name: String
  }

  input JoinerInput {
    name: String
    role: String
    ANDtitle: String
    level: Level
  }

  type Query { # Top level entry point for reads
    AND: AND
    searchByName(contains: String): [SearchResult]
    books: [Book!]!
  }

  type Mutation {
    newJoiner(club: ClubInput, joiner: JoinerInput): ANDI
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
  Date: dateScalar,
  SearchResult: {
    __resolveType(obj, context, info) {
      if (obj.peoplelead) {
        return "Club";
      }

      return "Hub";
    },
  },
  Book: {
    __resolveType(book, context, info) {
      if (book.courses) {
        return "Textbook";
      }

      if (book.colors) {
        return "ColoringBook";
      }

      return null;
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
    books: () => books,
  },
  Mutation: {
    newJoiner: (parent, args, context, info) => {
      console.log(JSON.stringify(args));
      // Add to database or service
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

/*
    mutation AddNewANDI($c: ClubInput, $j: JoinerInput) {
    newJoiner(club: $c, joiner: $j) {
        name
    }
    }
*/
