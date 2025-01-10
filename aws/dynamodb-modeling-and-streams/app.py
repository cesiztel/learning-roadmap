#!/usr/bin/env python3
import os
import aws_cdk as cdk
from dynamodb_modeling_and_streams.dynamodb_modeling_and_streams_stack import (
    DynamodbModelingAndStreamsStack,
)


app = cdk.App()
DynamodbModelingAndStreamsStack(app, "DynamodbModelingAndStreamsStack")

app.synth()
