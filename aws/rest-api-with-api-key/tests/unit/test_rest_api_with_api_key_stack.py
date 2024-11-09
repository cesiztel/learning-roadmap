import aws_cdk as core
import aws_cdk.assertions as assertions

from rest_api_with_api_key.rest_api_with_api_key_stack import RestApiWithApiKeyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rest_api_with_api_key/rest_api_with_api_key_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RestApiWithApiKeyStack(app, "rest-api-with-api-key")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
