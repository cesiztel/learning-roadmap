const ANDIs = [
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
        level: "L3.1",
      },
    ],
  },
];

exports.Aletta = Aletta;
exports.Dekker = Dekker;
