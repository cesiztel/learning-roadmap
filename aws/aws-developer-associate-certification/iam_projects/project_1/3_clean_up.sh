ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Remove users from groups
aws iam remove-user-from-group --user-name alice --group-name dev-group
aws iam remove-user-from-group --user-name bob   --group-name audit-group

# Delete access keys (list first to get the key ID)
alice_key=$(aws iam list-access-keys --user-name alice --query 'AccessKeyMetadata[0].AccessKeyId' --output text)
bob_key=$(aws iam list-access-keys --user-name bob --query 'AccessKeyMetadata[0].AccessKeyId' --output text)

aws iam delete-access-key --user-name alice --access-key-id $alice_key
aws iam delete-access-key --user-name bob   --access-key-id $bob_key

# Detach policies from groups
aws iam detach-group-policy --group-name dev-group \
  --policy-arn arn:aws:iam::$ACCOUNT_ID:policy/dev-s3-policy
aws iam detach-group-policy --group-name audit-group \
  --policy-arn arn:aws:iam::ACCOUNT_ID:policy/audit-s3-policy

# Delete groups and users
aws iam delete-group --group-name dev-group
aws iam delete-group --group-name audit-group
aws iam delete-user --user-name alice
aws iam delete-user --user-name bob

# Delete the policies
aws iam delete-policy --policy-arn arn:aws:iam:$ACCOUNT_ID:policy/dev-s3-policy
aws iam delete-policy --policy-arn arn:aws:iam::$ACCOUNT_ID:policy/audit-s3-policy

# Delete the bucket
aws s3 rb s3://iam-lab-$ACCOUNT_ID --force