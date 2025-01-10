from aws_cdk import (
    Stack,
    aws_lambda_event_sources as eventsources,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    Duration
)
from constructs import Construct


class DynamodbModelingAndStreamsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the lambda trigger of the stream
        new_order_processor = _lambda.Function(
            scope=self,
            id="NewOrderProcessorStreamFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            timeout=Duration.seconds(300),
            function_name="online-shop-new-order-processor-function",
            description="Function that process all the new orders of the shop",
            code=_lambda.Code.from_asset("assets/new_order_processor"),
            handler="index.lambda_handler",
            memory_size=128
        )


        # Explain the different types of StreamViewType
        data_store_table = dynamodb.Table(
            self, 
            "OnLineShopDataStoreTable",
            table_name="online-shop-data-store",
            partition_key=dynamodb.Attribute(
                name="PK",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="SK",
                type=dynamodb.AttributeType.STRING
            ),
            stream=dynamodb.StreamViewType.NEW_IMAGE
        )

        # Set the lambda function as trigger of the function
        new_order_processor.add_event_source(
            eventsources.DynamoEventSource(
                table=data_store_table,
                starting_position=_lambda.StartingPosition.LATEST,
                metrics_config=_lambda.MetricsConfig(
                    metrics=[_lambda.MetricType.EVENT_COUNT]
                )
            )
        )
