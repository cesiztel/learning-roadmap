const { ApolloServer, gql } = require('apollo-server');
const { PubSub } = require('apollo-server');

const pubsub = new PubSub();
const BOOK_ADDED = 'BOOK_ADDED';

// A schema is a collection of type definitions (hence "typeDefs")
// that together define the "shape" of queries that are executed against
// your data.
const typeDefs = gql`
  type Subscription {
    bookAdded: Book
  }

  type Mutation {
    addBook(title: String, authorName: String): Book
  }

  type Book {
    title: String
    author: Author
  }
  
  type Author {
    name: String
    books: [Book]
  }

  type Query {
      books: [Book] 
  }
`;

// Resolvers define the technique for fetching the types defined in the
// schema. This resolver retrieves books from the "books" array above.
const resolvers = {
    Subscription: {
        bookAdded: {
          // Additional event labels can be passed to asyncIterator creation
          subscribe: () => pubsub.asyncIterator([BOOK_ADDED]),
        },
    },
    Query: {
        books: () => books
    },
    Mutation: {
        addBook(root, args, context) {
            pubsub.publish(BOOK_ADDED, { bookAdded: args });

            return {
                title: args.title,
                author: { name: args.authorName },
            }
        },
    },
};

// The ApolloServer constructor requires two parameters: your schema
// definition and your set of resolvers.
const server = new ApolloServer({ typeDefs, resolvers });

// The `listen` method launches a web server.
server.listen().then(({ url, subscriptionsUrl }) => {
  console.log(`🚀 Server ready at ${url}`);
  console.log(`🚀 Subscriptions ready at ${subscriptionsUrl}`);
});

const books = [
    {
        title: 'Harry Potter and the Chamber of Secrets',
        author: { name: 'J.K. Rowling'},
    },
    {
        title: 'Jurassic Park',
        author: { name: 'Michael Crichton'},
    },
    {
        title: 'The Positronic Man ',
        author: { name: 'Isaac Asimov'}
    },
    {
        title: 'Foundation',
        author: { name: 'Isaac Asimov'}
    }
];