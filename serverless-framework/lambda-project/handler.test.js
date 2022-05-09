const handler = require("./handler");

test("Given name, hello returns 200 and correct body payload", async () => {
  const event = { name: "Antonio" };
  const expectedPayload = {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: "Go Serverless v1.0! Your function executed successfully!",
        input: event,
      },
      null,
      2
    ),
  };
  const helloResult = await handler.hello(event);

  expect(helloResult).toStrictEqual(expectedPayload);
});
