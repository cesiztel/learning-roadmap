# Set up account. 

Remember the way to setup the account:
*Least privilege principle*

- Create a new user with no privileges
- Setup the CLI with that user
- Do not give access through CLI to the root user

```
$ aws configure

// have multiple users in the same computer
$ aws configure --profile [profile_name] 

$ ~/.aws/credentials 
```

# AWS CLI

```
// Use specific profile in the request (only see what 
// the profile is allow)
aws s3 ls --profile [profile_name]
```

# AWS CLI S3

```
aws <service> <action> <options>

// List all the buckets
$ aws s3 ls  

// List the content of specific bucket
$ aws s3 ls s3://bucket_name

// Copy file to certain bucket (upload)
$ aws s3 cp <local_file> s3://bucket_name

// Copy folder content to certain bucket (upload)
$ aws s3 cp <local_file> s3://bucket_name

// Copy bucket file to local (download)
$ aws s3 cp s3://bucket_name/file_name <local_folder>
```
