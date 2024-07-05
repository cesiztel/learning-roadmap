import aws_cdk as core
import aws_cdk.assertions as assertions

from electrical_vehicles_with_open_data.electrical_vehicles_with_open_data_stack import ElectricalVehiclesWithOpenDataStack

# example tests. To run these tests, uncomment this file along with the example
# resource in electrical_vehicles_with_open_data/electrical_vehicles_with_open_data_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ElectricalVehiclesWithOpenDataStack(app, "electrical-vehicles-with-open-data")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
