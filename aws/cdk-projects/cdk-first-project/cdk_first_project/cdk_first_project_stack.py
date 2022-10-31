from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)

class CdkFirstProjectStack(Stack):

    def __init__(
        self, 
        scope: Construct,
        construct_id: str,
        **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Add powertools as lambda layer
        powertools_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            id="lambda-powertools",
            layer_version_arn=f"arn:aws:lambda:{self.region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:12"
        )

        # Create lambda and add Power tools
        _lambda.Function(
            self,
            'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
            layers=[powertools_layer]
        )