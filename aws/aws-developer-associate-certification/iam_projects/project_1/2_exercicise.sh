#!/bin/bash
BUCKET="your-bucket-name"

echo "=== Testing as alice (developer) ==="
# Should succeed
aws s3 cp /tmp/test.txt s3://$BUCKET/test.txt --profile alice && echo "PUT: OK"
aws s3 ls s3://$BUCKET --profile alice           && echo "LIST: OK"
aws s3 cp s3://$BUCKET/test.txt /tmp/ --profile alice && echo "GET: OK"

echo ""
echo "=== Testing as bob (auditor) ==="
# LIST and GET should succeed
aws s3 ls s3://$BUCKET --profile bob             && echo "LIST: OK"
aws s3 cp s3://$BUCKET/test.txt /tmp/ --profile bob && echo "GET: OK"

# PUT should fail with AccessDenied
aws s3 cp /tmp/test.txt s3://$BUCKET/bob.txt --profile bob \
  && echo "PUT: OK (unexpected!)" \
  || echo "PUT: DENIED (expected)"