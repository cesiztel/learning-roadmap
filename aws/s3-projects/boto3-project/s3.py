import boto3
import logging
from botocore.exceptions import ClientError

client = boto3.client("s3")

# List all the buckets
response = client.list_buckets()
print(response)

# Generate presigned Url


def generate_presigned_url(client, bucket_name, object_name, expiration=60):
    try:
        response = client.generate_presigned_url('get_object',
                                                 Params={'Bucket': bucket_name,
                                                         'Key': object_name},
                                                 ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    return response


print(generate_presigned_url(client, 'invented-bucket', 'cat1.jpeg'))
