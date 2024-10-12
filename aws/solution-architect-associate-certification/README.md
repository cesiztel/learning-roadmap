# AWS Solutions Architect Associate Certification Path

## Introduction

This repository contains learning projects which I did during the preparation for the AWS-SAA certification exam. 

## Table of Contents

 1. [Identity and Access Management](#identity-and-access-management)
 2. [Simple Storage Service](#s3)

## Identity and Access Management

### Projects

**Project: Manage users, groups and test permissions and access.**

1. Create user called john-doe.
2. Create user called maria-doe
3. Create user called tester-doe

Practice to create the user without access to the console and only programmatic access. Configure
the user profiles in your computer to run commands. Install the AWS CLI.

4. Create 2 groups: Admins, Testers.
5. Create an S3 bucket on the region configure on the profile.Should be unique name.
6. Run the following commands using any of the created users (via profile)

```bash
aws s3 ls --profile=john-doe
```
All the execution should return access denied with any of the profiles.

7. Add to the testers group the managed policy `AmazonS3ReadOnlyAccess`. This will be read only permissions but will prevent to that group CUD actions on the bucket.
8. Add the user tester-doe to that group and run again the command:
```bash
aws s3 ls --profile=tester-doe
```
As result the list of buckets should be listed. Other user will give the denied error.

9. Using the tester doe, try to copy a file to the bucket using the following:
```bash
aws s3 cp ./file_to_upload_to_s3.txt s3://[name_of_the_bucket_you_use] --profile=tester-doe
```
The access should be denied for this operations.

10. Add to the admin group, john and maria. And now add the permissions `AmazonS3FullAccess`
11. Try to run the command with the profile of john or maria. It will work.
12. To finish the project: Delete the users, the groups, users, the local profiles and the S3 bucket (before you will need to empty it)

## Simple Storage Service

### Projects

- [Tutorial: Hosting on-demand streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-cloudfront-route53-video-streaming.html)

