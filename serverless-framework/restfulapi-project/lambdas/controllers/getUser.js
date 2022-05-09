const Responses = require("../common/API_Responses")
// const users = require("../data/users")
const Dynamo = require("../common/Dynamo")

const tableName = process.env.tableName

exports.handler = async (event) => {
    if (!event.pathParameters || !event.pathParameters.ID) {
        return Responses._400({ message: 'missing the ID from the path '})
    }

    let ID = event.pathParameters.ID

    const user = await Dynamo.get(ID, tableName).catch(err => {
        console.log("error in Dynamo Get", err)

        return Responses._500( { message: 'error getting data from database!'})
    })

    if (!user) {
        return Responses._404({ message: 'user not found!'})
    }

    return Responses._200(user);
};