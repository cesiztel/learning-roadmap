const { ApolloServer, gql } = require('apollo-server');
const universe = require('./universe');

const starWarsUniverse = universe.buildUniverse();

const typeDefs = gql``;

const resolvers = {};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url, subscriptionsUrl }) => {
  console.log(`🚀 Server ready at ${url}`);
  console.log(`🚀 Subscriptions ready at ${subscriptionsUrl}`);
});
