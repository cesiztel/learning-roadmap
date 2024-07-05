from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_
)
from constructs import Construct

class ElectricalVehiclesWithOpenDataStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        data_processor = lambda_.Function(
            self, 
            "ElectricalVehicleDataProcessor",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset("src/data_processor"),
            handler="index.handler",
        )
