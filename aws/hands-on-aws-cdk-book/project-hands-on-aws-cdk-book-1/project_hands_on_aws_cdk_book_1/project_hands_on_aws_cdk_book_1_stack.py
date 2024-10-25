from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct
from project_hands_on_aws_cdk_book_1.constructs.custom_s3_bucket import Custom3BucketProperties, Custom3Bucket

class ProjectHandsOnAwsCdkBook1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # L1 S3 bucket code
        s3.CfnBucket(
            self,
            "RawDataBucketL1",
            bucket_name="raw-data-landing-zone-greeting-l1",
            access_control="Private",
            bucket_encryption=s3.CfnBucket.BucketEncryptionProperty(
                server_side_encryption_configuration=[s3.CfnBucket.ServerSideEncryptionRuleProperty(
                    bucket_key_enabled=False,
                    server_side_encryption_by_default=s3.CfnBucket.ServerSideEncryptionByDefaultProperty(
                        sse_algorithm="aws:kms",
                    )
                )]
            ),
            versioning_configuration=s3.CfnBucket.VersioningConfigurationProperty(
                status="Enabled"
            )
        )

        # L2 S3 bucket code
        s3.Bucket(
            self,
            "RawDataBucketL2",
            bucket_name="raw-data-landing-zone-greeting-l2",
            encryption=s3.BucketEncryption.KMS,
            versioned=True
        )

        # L3 S3 bucket
        Custom3Bucket(
            self, 
            "RawDataBucketL3",
            Custom3BucketProperties(
                bucket_name="raw-data-landing-zone-greeting-l3",
                expiration_days=120
            )
        )
