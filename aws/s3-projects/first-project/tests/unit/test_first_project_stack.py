import aws_cdk as core
import aws_cdk.assertions as assertions

from first_project.first_project_stack import FirstProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in first_project/first_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FirstProjectStack(app, "first-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
