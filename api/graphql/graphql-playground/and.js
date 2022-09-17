const ANDIs = [
  {
    name: "Harry Potter",
    role: "Product Developer",
    ANDtitle: "wizard beginner",
    level: "L1.1",
  },
  {
    name: "Magneto",
    role: "Product Analyst",
    ANDtitle: "people hater",
    level: "L6",
  },
  {
    name: "Lobezno",
    role: "People lead",
    ANDtitle: "people hater",
    level: null,
  },
  {
    name: "Harley Queen",
    role: "Club executive",
    ANDtitle: "crazyness lover",
    level: null,
  },
  {
    name: "Deadpool",
    role: "Hub executive",
    ANDtitle: "jokes lover",
    level: null,
  },
  {
    name: "Kaarline",
    role: "People lover",
    ANDtitle: "people lover",
    level: null,
  },
  {
    name: "Maaike",
    role: "Club executive",
    ANDtitle: "pizza lover",
    level: null,
  },
  {
    name: "Paramjit",
    role: "Chief Executive Officer",
    ANDtitle: "foddy",
    level: null,
  },
  {
    name: "Jeroen",
    role: "Hub executive",
    ANDtitle: "Stone head",
    level: null,
  },
  {
    name: "Tom Pope",
    role: "Product Developer",
    ANDtitle: "GraphQL lover",
    level: "L3.1",
  },
  {
    name: "Evelyn",
    role: "UX Principal",
    ANDtitle: "Design lover",
    level: "L6",
  },
];

const AND = {
  ceo: ANDIs.find((andi) => andi.name === "Paramjit"),
  hubs: [
    {
      name: "Benelux",
      executive: ANDIs.find((andi) => andi.name === "Jeroen"),
      clubs: [
        {
          name: "Aletta",
          executive: ANDIs.find((andi) => andi.name === "Maaike"),
          peoplelead: ANDIs.find((andi) => andi.name === "Kaarline"),
          squads: [
            {
              name: "Squad1",
              lead: ANDIs.find((andi) => andi.name === "Evelyn"),
              members: [ANDIs.find((andi) => andi.name === "Tom Pope")],
            },
          ],
        },
      ],
    },
    {
      name: "London North",
      executive: ANDIs.find((andi) => andi.name === "Deadpool"),
      clubs: [
        {
          name: "Dekker",
          executive: ANDIs.find((andi) => andi.name === "Harley Queen"),
          peoplelead: ANDIs.find((andi) => andi.name === "Lobezno"),
          squads: [
            {
              name: "Squad1",
              lead: ANDIs.find((andi) => andi.name === "Magneto"),
              members: [ANDIs.find((andi) => andi.name === "Harry Potter")],
            },
          ],
        },
      ],
    },
  ],
};

const books = [
  {
    title: "This is a query language",
    author: {
      name: "asdajsdada",
    },
    courses: [
      {
        name: "course of the graphql",
      },
      {
        name: "course of the x",
      },
    ],
    date: new Date(),
  },
  {
    title: "This is another query",
    author: {
      name: "eghjskadfhg",
    },
    colors: ["red", "green"],
    date: new Date(),
  },
];

exports.ANDIs = ANDIs;
exports.AND = AND;
exports.books = books;
