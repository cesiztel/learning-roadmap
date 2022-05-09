const Responses = require("../common/API_Responses")
// const users = require("../data/users")
const Dynamo = require("../common/Dynamo")

const tableName = process.env.tableName

exports.handler = async () => {
    const users = await Dynamo.all(tableName).catch(err => {
        console.log("error in Dynamo Get", err)

        return Responses._500( { message: 'error getting data from database!'})
    })

    return Responses._200(users)
};