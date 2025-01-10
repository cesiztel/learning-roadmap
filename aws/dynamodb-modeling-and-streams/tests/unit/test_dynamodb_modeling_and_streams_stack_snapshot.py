import aws_cdk as cdk
from aws_cdk.assertions import Template

from dynamodb_modeling_and_streams.dynamodb_modeling_and_streams_stack import (
    DynamodbModelingAndStreamsStack,
)


# The snapshot parameter is injected by Pytest -- it's a fixture provided by
# syrupy, the snapshot testing library we're using:
# https://docs.pytest.org/en/stable/fixture.html
def test_matches_snapshot(snapshot):
    # Set up the app and resources in the other stack.
    app = cdk.App()

    # Create main DynamodbModelingAndStreamsStack 
    stack = DynamodbModelingAndStreamsStack(app, "dynamodb-modeling-and-streams")

    # Prepare the stack for assertions.
    template = Template.from_stack(stack)

    assert template.to_json() == snapshot
