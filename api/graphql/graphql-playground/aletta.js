const ANDIs = [
  {
    name: "Tom Pope",
    role: "Product Developer",
    ANDtitle: "GraphQL lover",
  },
  {
    name: "Evelyn",
    role: "UX Principal",
    ANDtitle: "Design lover",
  },
];

const Aletta = [
  {
    name: "Squad1",
    lead: ANDIs.find((andi) => andi.name === "Evelyn"),
    members: [ANDIs.find((andi) => andi.name === "Tom Pope")],
  },
];

const Dekker = [
  {
    name: "Squad1",
    lead: null,
    members: [
      {
        name: "John Wick",
        role: "Product Analyst",
        ANDtitle: "Killing lover",
      },
    ],
  },
];

exports.Aletta = Aletta;
exports.Dekker = Dekker;
