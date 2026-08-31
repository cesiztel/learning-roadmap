import aws_cdk as core
import aws_cdk.assertions as assertions

from multi_account_vpc_ram.multi_account_vpc_ram_stack import MultiAccountVpcRamStack

# example tests. To run these tests, uncomment this file along with the example
# resource in multi_account_vpc_ram/multi_account_vpc_ram_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MultiAccountVpcRamStack(app, "multi-account-vpc-ram")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
