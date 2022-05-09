## Useful commands

- Deploy application

```
serverless deploy --aws-profile mydefaulttestprof --region eu-west-2
```

- Invoke lambda

```
aws lambda invoke --function-name serverless-framework-dev-hello \
    --cli-binary-format raw-in-base64-out \
    --payload '{"name": "John Smith"}' \
    response.json
```
