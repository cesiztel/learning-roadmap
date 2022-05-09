const Responses = require('../common/API_Responses')
const Dynamo = require('../common/Dynamo')

const tableName = process.env.tableName;

exports.handler = async (event) => {
    const user = JSON.parse(event.body)

    const newUser = await Dynamo.save(user, tableName).catch(err => {
        console.log("error in Dynamo Get", err)

        return Responses._500( { message: 'error saving operation!'})
    })

    if (!newUser) {
        return Responses._500({ message: 'error saving user!'})
    }

    return Responses._200(newUser);
};