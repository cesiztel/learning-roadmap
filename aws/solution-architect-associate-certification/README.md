# AWS Solutions Architect Associate Certification Path

## Introduction

This repository contains resources, links to documentation and blogs post and learning projects which I did during the preparation for the AWS-SAA certification exam. 

## Table of Contents

 1. [Identity and Access Management](#identity-and-access-management)

## Identity and Access Management

IAM is a global service

### Building blocks of IAM

- **Users**: A physical person (one per user). Do not share users.
- **Groups**: functions as administration, developer. Contains users.
- **Roles**: Delegation permissions
- **IAM Policy documents**: assign permissions declaring in a JSON document

You can assign policy documents to Groups, Users and Roles.

Best practices is assigned documents to Groups instead of Users, because is harder to maintain if you do individually.

- The principle of least privilege: Only assign a user the minimum amount of privileges they need to do their job.

### Connecticting to IdP (Identity Provider)

Supported provider types:
- SAML
- OpenID Connect

### Securing root account

- In this link can be found the [root user best practices for your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#ru-bp-secure)

Summary:
- Activate MFA.
- Do not share the root user password
- Do not store the root user password on dependent AWS services.
- Do not create access keys for the root user.

### Using IAM Policy Documents

- Official AWS documentation for this [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

Example of policy document:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

Explanation of the document schema. If it's not specified the field as Optional, means that the field is mandatory:

- **Version**: Specify the version of the policy language that you want to use. Recommended `2012-10-17`.
- **Statement**: Use this main policy element as a container for the following elements. You can include more than one statement in a policy.
- **Sid** (Optional) – Include an optional statement ID to differentiate between your statements.
- **Effect** – Use Allow or Deny to indicate whether the policy allows or denies access.
- **Principal** (Required in only some circumstances) - If it's create a resource based policy then is required to indicate the identity which you would like to allow or deny. If the policy is attached to a user or role, then it's implied, because who assume that policy is itself.
- **Action** – Include a list of actions that the policy allows or denies.
- **Resource** (Required in only some circumstances) – If you create an IAM permissions policy, you must specify a list of resources to which the actions apply. If you create a resource-based policy, this element is optional. If you do not include this element, then the resource to which the action applies is the resource to which the policy is attached.
- **Condition** (Optional) – Specify the circumstances under which the policy grants permission.

### Quiz questions

- Why are IAM users considered "permanent" users?
Because once their password, access key, or secret key is set, these credentials don't automatically rotate or change without human interaction. For the password, you need to set the rotation policy yourself.

### Projects

**Project: Manage users, groups and test permissions and access.**

1.- Create user called john-doe
2.- Create user called maria-doe
3.- Create user called tester-doe
Practice to create the user without access to the console and only programmatic access. Configure
the user profiles in your computer to run commands. Install the AWS CLI
4.- Create 2 groups: Admins, Testers.
5.- Create an S3 bucket on the region configure on the profile. Should be unique name.
6.- Run the following commands using any of the created users (via profile)

```bash
aws s3 ls --profile=john-doe
```
All the execution should return access denied with any of the profiles.
7.- Add to the testers group the managed policy `AmazonS3ReadOnlyAccess`. This will be read only permissions but will prevent to that group CUD actions on the bucket.
8.- Add the user tester-doe to that group and run again the command:
```bash
aws s3 ls --profile=tester-doe
```
As result the list of buckets should be listed. Other user will give the denied error.
9.- Using the tester doe, try to copy a file to the bucket using the following:
```bash
aws s3 cp ./file_to_upload_to_s3.txt s3://[name_of_the_bucket_you_use] --profile=tester-doe
```
The access should be denied for this operations.
10.- Add to the admin group, john and maria. And now add the permissions `AmazonS3FullAccess`
11.- Try to run the command with the profile of john or maria. It will work.
12.- To finish the project: Delete the users, the groups, users, the local profiles and the S3 bucket (before you will need to empty it)
