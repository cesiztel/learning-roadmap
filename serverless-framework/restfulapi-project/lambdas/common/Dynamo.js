const AWS = require('aws-sdk')

const documentClient = new AWS.DynamoDB.DocumentClient()

const Dynamo = {
    async save(user, TableName) {
        const params = {
            TableName,
            Item: user
        }

        const res = await documentClient.put(params).promise();

        if (!res) {
            throw Error(`There was an error inserting user with ID:${user.ID}`)
        }

        return user
    },
    async all(TableName) {
        const params = {
            TableName
        }

        const data = await documentClient
            .scan(params)
            .promise()

        console.log(data);
        if (!data || !data.Items) {
            throw Error(`Get users does not found`)
        }

        return data.Items
    },
    async get(ID, TableName) {
        const params = {
            TableName,
            Key: {
                ID
            }
        }

        const data = await documentClient
            .get(params)
            .promise()

        if (!data || !data.Item) {
            throw Error(`User ID:${ID} not found`)
        }

        return data.Item
    }
}

module.exports = Dynamo