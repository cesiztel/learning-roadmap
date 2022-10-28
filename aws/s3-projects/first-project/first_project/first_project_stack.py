from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_s3 as s3
)
from constructs import Construct


class FirstProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a bucket with random name + id
        # s3.Bucket(self, id="MyBucket")
        # Create abucket with name + id
        # s3.Bucket(self, id="MyBucket2", bucket_name="my-bucket-name")
        # When we do `cdk destroy` the S3 gets orphan because are not destroy
        s3.Bucket(
            self,
            id="MyBucket",
            bucket_name="my-bucket-name-23",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
        # If we do not use removal policy and auto_delete and change the name
        # of the bucket, the old bucket will be still there. Take in account
        # change the name of the bucket and removing the bucket to create
        # a new name can cause data losses.

        # Lifecycle rules
        lyfecycle_rule = s3.LifecycleRule(
            transitions=[
                s3.Transition(
                    storage_class=s3.StorageClass.GLACIER_INSTANT_RETRIEVAL,
                    transition_after=Duration.days(1)
                ),
                s3.Transition(
                    storage_class=s3.StorageClass.GLACIER,
                    transition_after=Duration.days(3)
                )
            ]
        )

        s3.Bucket(
            self,
            id="MyBucketWithLifecycle",
            bucket_name="my-bucket-with-life-cycle",
            lifecycle_rules=[lyfecycle_rule],
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )