import aws_cdk as core
import aws_cdk.assertions as assertions

from project_hands_on_aws_cdk_book_1.project_hands_on_aws_cdk_book_1_stack import ProjectHandsOnAwsCdkBook1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_hands_on_aws_cdk_book_1/project_hands_on_aws_cdk_book_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectHandsOnAwsCdkBook1Stack(app, "project-hands-on-aws-cdk-book-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
