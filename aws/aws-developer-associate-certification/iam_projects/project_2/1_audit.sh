#!/bin/bash
set -euo pipefail

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET_NAME="iam-lab-${ACCOUNT_ID}"
USERS=("alice" "bob")

echo "============================================"
echo " IAM Access Audit Report"
echo " Bucket: $BUCKET_NAME"
echo "============================================"

for USER in "${USERS[@]}"; do
  USER_ARN="arn:aws:iam::${ACCOUNT_ID}:user/${USER}"
  echo ""
  echo "--- User: $USER ---"

  echo "  Bucket-level actions:"
  aws iam simulate-principal-policy \
    --policy-source-arn "$USER_ARN" \
    --action-names s3:ListBucket \
    --resource-arns "arn:aws:s3:::${BUCKET_NAME}" \
    --query 'EvaluationResults[*].{Action:EvalActionName, Decision:EvalDecision}' \
    --output table

  echo "  Object-level actions:"
  aws iam simulate-principal-policy \
    --policy-source-arn "$USER_ARN" \
    --action-names s3:GetObject s3:PutObject s3:DeleteObject \
    --resource-arns "arn:aws:s3:::${BUCKET_NAME}/*" \
    --query 'EvaluationResults[*].{Action:EvalActionName, Decision:EvalDecision}' \
    --output table
done