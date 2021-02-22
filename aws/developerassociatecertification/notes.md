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

// Copy folder content to certain bucket (upload all)
$ aws s3 cp <local_folder> s3://bucket_name --recursive

// Sync folder to certain bucket (sync all)
$ aws s3 sync <local_folder> s3://bucket_name

// Copy bucket file to local (download)
$ aws s3 cp s3://bucket_name/file_name <local_folder>
```

Remember that S3 is an object storage, so we do not have folder structures. But we can create prefix, which simulates a folder structure. In a URI

`s3://bucket_name/whatever` The last component (whatever) is a prefix which can simulate a local folder structure like:
```
whatever
  |- File 1
  |- File 2
```

# AWS CLI EC2

```
// Start instance
$ aws ec2 run-instances \
      --image-id <ami-072571fe035924fa7> \
      --count 1 \
      --instance-type <t2.micro> \
      --key-name <whateverkeyname> \
      --security-group-ids <> \
      --subnet-id <> \

// List instances
$ aws ec2 describe-instances --filters "Name-Instance-Type,Value=t2.micro" --query "Reservations[].Instances[].InstanceId"

// Terminate the instance
$ aws ec2 terminate-instances --instance-ids <instance-id>
```