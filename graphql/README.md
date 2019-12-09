# GraphQL

# Introduction
GraphQL has its own type system that’s used to define the schema of an API. The syntax for writing schemas is called Schema Definition Language (SDL).

## 1. The Schema Definition Language (SDL)

```
type Character {
    name: String!
    appearsIn: [Episode!]]!
}
```
This is basic type. The type has fields. One field is `String` and the other one is and array `[]` of type `Episode`. String in GraphQL langugae is called `scalar`. The `!` represents that the field is required.

We can create hierarchies of objects nesting types:

```
type Character {
    name: String!
    appearsIn: [Episode!]]!
}

type Episode {
    name: String!
}
```
GraphQL comes with a set of default scalar types out of the box:

- `Int` 
- `Float`
- `String`
- `Boolean`
- `ID`: represents unique identifier, usually used to refetch an object or as the key for the cache.
- You can create custom scalars, like:
    ex: `scalar Date` How to serialize and deserialize the scalar type is up to the resolver implementation.
- Enums

```
enum Episode {
    NEWHOPE
    EMPIRE
    JEDI
}
```
This means that wathever we use the type `Episode` in our schema, we expect it to be exactly one of `NEWHOPE`, `NEWHOPE`, `JEDI`.

### 1.1 Interfaces
----

Like many type systems, GraphQL supports interfaces. An Interface is an abstract type that includes a certain set of fields that a type must include to implement the interface.

Example:

```
interface Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
}

type Human implements Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
    starships: [Starship]
    totalCredits: Int
}

type Droid implements Character {
    id: ID!
    name: String!
    friends: [Character]
    appearsIn: [Episode]!
    primaryFunction: String
}
```

### 1.2 Union types
----

Union types are very similar to interfaces, but they don't get to specify any common fields between the types.

```
union Galaxy = Human | Droid | Starship
```

### 1.3 Inpuy types
----

With input types you can pass to query complex objects. This is particularly valuable in the case of mutations, where you might want to pass in a whole object to be created

```
input ReviewInput {
  stars: Int!
  commentary: String
}
```

## 2. Queries and mutations

Query is one of the operations that you can do againts your GraphQL API's. When you do queries, you asking GraphQL for fields of certain objects. You can see immediately that the query has exactly the same shape as the result. This is essential to GraphQL, because you always get back what you expect, and the server knows exactly what fields the client is asking for. This is one of the benefits of using GraphQL. So, the GraphQL API's are self documentated.

Sample query using shorthand syntax:

```
{
  hero {
    name
  }
}
```

We can use opereation name. This practices is recommended en production environments. The first word `query`, indicates which operation we are going to perform. The second part of the operator is unique operation name. It is only required in multi-operation documents, but its use is encouraged because it is very helpful for debugging and server-side logging

```
query HeroNameAndFriends {
  hero {
    name
  }
}
```

### 2.1 Query fields
----

Example 

Query:
```
{
  hero {
    name
  }
}
```
Result:
```
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```

### 2.1 Query arguments & aliases
----

Example

```
{
  human(id: "1000") {
    name
    height
  }
}
```

Every field and nested object can get its own set of arguments, making GraphQL a complete replacement for making multiple API fetches. So this is very convenient, to avoid to make multiple requests to get specific resource as we would do in REST. We can pass arguments in the same fashion way as programming language function signatures.

```
{
  human(id: "1000") {
    name
    height(unit: FOOT)
  }
}
```

You can't directly query for the same field with different arguments. That's why you need aliases - they let you rename the result of a field to anything you want.

```
{
  empireHero: hero(episode: EMPIRE) {
    name
  }
  jediHero: hero(episode: JEDI) {
    name
  }
}
```

### 2.2 Fragments

GraphQL includes reusable units called fragments. Fragments let you construct sets of fields, and then include them in queries where you need to.

```
{
  empireHero: hero(episode: EMPIRE) {
    ...comparisonHero
  }
  jediHero: hero(episode: JEDI) {
    ...comparisonHero
  }
}

fragment comparisonHero on Character {
  name
  appearsIn
  friends {
    name
  }
}
```

It is possible for fragments to access variables declared in the query or mutation

```
query HeroComparison($first: Int = 3) {
  empireHero: hero(episode: EMPIRE) {
    ...comparisonHero
  }
  jediHero: hero(episode: JEDI) {
    ...comparisonHero
  }
}

fragment comparisonHero on Character {
  name
  friendsConnection(first: $first) {
    totalCount
    edges {
      node {
        name
      }
    }
  }
}
```

### 2.3 Variables

GraphQL has a first-class way to factor dynamic values out of the query, and pass them as a separate dictionary. These values are called variables.

When we start working with variables, we need to do three things:

- Replace the static value in the query with `$variableName`
- Declare `$variableName` as one of the variables accepted by the query
- Pass `variableName: value` in the separate, transport-specific (usually JSON) variables dictionary

```
query HeroNameAndFriends($episode: Episode) {
  hero(episode: $episode) {
    name
    friends {
      name
    }
  }
}

// Variable

{
  "episode": "JEDI"
}
```
All declared variables must be either scalars, enums, or input object types

```
query HeroNameAndFriends($episode: Episode = JEDI) {
  hero(episode: $episode) {
    name
    friends {
      name
    }
  }
}
```

Now, in our client code, we can simply pass a different variable rather than needing to construct an entirely new query

### 2.3 Directives

A directive can be attached to a field or fragment inclusion, and can affect execution of the query in any way the server desires. The core GraphQL specification includes exactly two directives, which must be supported by any spec-compliant GraphQL server implementation:

- `@include(if: Boolean)` Only include this field in the result if the argument is `true`
- `@skip(if: Boolean)` Skip this field if the argument is `true`

Server implementations may also add experimental features by defining completely new directives.

### 2.4 Inline fragments

If you are querying a field that returns an interface or a union type, you will need to use inline fragments to access data on the underlying concrete type

```
query HeroForEpisode($ep: Episode!) {
  hero(episode: $ep) {
    name
    ... on Droid {
      primaryFunction
    }
    ... on Human {
      height
    }
  }
}

{
  "ep": "JEDI"
}
```

### 2.5 Meta fields

Given that there are some situations where you don't know what type you'll get back from the GraphQL service, you need some way to determine how to handle that data on the client. GraphQL allows you to request `__typename`, a meta field, at any point in a query to get the name of the object type at that point.

```
{
  search(text: "an") {
    __typename
    ... on Human {
      name
    }
    ... on Droid {
      name
    }
    ... on Starship {
      name
    }
  }
}

{
  "data": {
    "search": [
      {
        "__typename": "Human",
        "name": "Han Solo"
      },
      {
        "__typename": "Human",
        "name": "Leia Organa"
      },
      {
        "__typename": "Starship",
        "name": "TIE Advanced x1"
      }
    ]
  }
}
```

## 3. Mutations

There generally are three kinds of mutations:

- creating new data
- updating existing data
- deleting existing data

Mutations follow the same syntactical structure as queries, but they always need to start with the `mutation` keyword

```
input CharacterInput {
    name: String!
    appearsIn: [Episode!]]!
}
```
We need to declare the inputs and types that we are going to pass to the mutation. The mutations are declared as other type:

```
type Mutation {
    createHero(character: CharacterInput!): Character
}
```

A mutation can contain multiple fields, just like a query. There's one important distinction between queries and mutations, other than the name:

While query fields are executed in parallel, mutation fields run in series, one after the other.

## Realtime Updates with Subscriptions

Another important requirement for many applications today is to have a realtime connection to the server in order to get immediately informed about important events. For this use case, GraphQL offers the concept of subscriptions.

When a client subscribes to an event, it will initiate and hold a steady connection to the server. Whenever that particular event then actually happens, the server pushes the corresponding data to the client. Unlike queries and mutations that follow a typical “request-response-cycle”, subscriptions represent a stream of data sent over to the client.

# Projects
Playground project: 

# Resources

- First GraphQL API: https://dev.to/augani/how-to-build-a-graphql-api-from-scratch-19c0
- Learn fundamentals: https://www.howtographql.com/basics/2-core-concepts/
