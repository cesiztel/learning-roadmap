from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_logs as logs
)
from constructs import Construct
from aws_cdk.aws_apigateway import IntegrationResponse, PassthroughBehavior, MethodResponse, UsagePlanPerApiStage

class RestApiWithApiKeyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the API
        library_api = apigateway.RestApi(
            self, 
            "MyLibraryApi",
            rest_api_name="MyLibrary"
        )
        # Add /books resource + GET method
        get_all_books = library_api.root.add_resource("books")
        get_all_books.add_method(
            "GET", 
            apigateway.MockIntegration(
                integration_responses=[
                    IntegrationResponse(status_code="200")
                ],
                passthrough_behavior=PassthroughBehavior.NEVER,
                request_templates={
                    "application/json": "{ 'statusCode': 200 }"
                },
            ),
            method_responses=[MethodResponse(status_code="200")],
            api_key_required=True
        )

        # Development stage
        dev_log_group = logs.LogGroup(self, "LibraryAPIDevLogs")
        development_stage = apigateway.Stage(
            self,
            "DevStage",
            stage_name="dev",
            deployment=library_api.latest_deployment,
            access_log_destination=apigateway.LogGroupLogDestination(dev_log_group),
            access_log_format=apigateway.AccessLogFormat.json_with_standard_fields(
                caller=False,
                http_method=True,
                ip=True,
                protocol=True,
                request_time=True,
                resource_path=True,
                response_length=True,
                status=True,
                user=True
            )
        )

        # Create usage plan
        # We need to associate the usage plan to an:
        # -> API Key
        # -> Stage
        # -> API
        library_api_usage_plan = library_api.add_usage_plan(
            id="LibraryAPIUsagePlan",
            name="LibraryAPIUsagePlan",
            api_stages=[
                UsagePlanPerApiStage(
                    api=library_api,
                    stage=development_stage
                )
            ],
            throttle=apigateway.ThrottleSettings(
                rate_limit=20,
                burst_limit=2
            ),
        )

        # Create API key
        library_api_key = library_api.add_api_key("LibraryAPIApiKey")
        # Attach key to the plan
        library_api_usage_plan.add_api_key(library_api_key)
