import aws_cdk as core
import aws_cdk.assertions as assertions

from dynamodb_modeling_and_streams.dynamodb_modeling_and_streams_stack import DynamodbModelingAndStreamsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dynamodb_modeling_and_streams/dynamodb_modeling_and_streams_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DynamodbModelingAndStreamsStack(app, "dynamodb-modeling-and-streams")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
