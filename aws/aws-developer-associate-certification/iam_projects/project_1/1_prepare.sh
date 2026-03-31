BUCKET_NAME="iam-lab-$(aws sts get-caller-identity --query Account --output text)"

aws s3api create-bucket \
    --bucket $BUCKET_NAME \
    --region eu-west-1 \
    --create-bucket-configuration LocationConstraint=eu-west-1

## Because API legacy, initialy all the buckets where create for us-east-1.
## If you want to use the regional endpoint to create the bucket on the
## specified region, then you need to use this flag, otherwise, the 
## API will trigger an error: bucket creation fails with a location error.
## Unless the bucket is created in us-east-1, then you can omit the flag and the bucket will be created in us-east-1 by default.

echo "============================================"
echo "Bucket ARN: arn:aws:s3:::$BUCKET_NAME"
echo "============================================"

aws iam create-user --user-name alice
aws iam create-user --user-name bob

# Verify both exist
aws iam list-users --query 'Users[*].UserName' --output table

# In the moment of creation the IAM does not have any 
# permissions. Implicit deny is the default.

echo "============================================"
echo "Users alice and bob created!"
echo "============================================"

aws iam create-policy \
  --policy-name dev-s3-policy \
  --policy-document file://dev-s3-policy.json \
  --description "Developer read/write access to iam-lab bucket"

aws iam create-policy \
  --policy-name audit-s3-policy \
  --policy-document file://audit-policy.json \
  --description "Auditor read-only access to iam-lab bucket"

# Note the ARNs printed — you need them in the next step
# Format: arn:aws:iam::ACCOUNT_ID:policy/dev-s3-policy


echo "============================================"
echo "Policies created!"
echo "============================================"

# Create groups
aws iam create-group --group-name dev-group
aws iam create-group --group-name audit-group

echo "============================================"
echo "Groups created!"
echo "============================================"

# Attach policies to groups (replace ACCOUNT_ID)
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

echo "============================================"
echo "Attach policies to the group!"
echo "============================================"

aws iam attach-group-policy \
  --group-name dev-group \
  --policy-arn arn:aws:iam::$ACCOUNT_ID:policy/dev-s3-policy

aws iam attach-group-policy \
  --group-name audit-group \
  --policy-arn arn:aws:iam::$ACCOUNT_ID:policy/audit-s3-policy\

echo "============================================"
echo "Adding users!"
echo "============================================"

aws iam add-user-to-group --user-name alice --group-name dev-group
aws iam add-user-to-group --user-name bob   --group-name audit-group

echo "============================================"
echo "Confirming membership!"
echo "============================================"

# Confirm membership
aws iam get-group --group-name dev-group
aws iam get-group --group-name audit-group

echo "============================================"
echo "Creating access keys. After creation, configure the credentials!"
echo "============================================"

# Create access keys for both users
aws iam create-access-key --user-name alice
aws iam create-access-key --user-name bob

