### Workshop

1. Create Stack using `pre-requisites.yaml`. That creates the instance role for the EC2 instance

2. Use reference architecture `architecture.drawio`
   * Build VPC A with CIDR block 10.0.0.0/16 and activate DNS resolution and DNS hostnames after creation.
   * Logically a subnet is a range of IP addresses in your VPC. Depending if the subnet is connected to internet is a public subnet or private subnet.
   * Network ACL (NACLs) are optional layer of security for your VPC (VPC level on the subnets) for controlling the traffic in and out of one of more subnets. How the NACLs rules works: Rules are evaluated in order from lowest to highest. If the traffic doesn’t match any rules, the * rule is applied, and the traffic is denied. Default NACLs allow all inbound and outbound traffic, as shown below, unless customized.
   
   How to combine security groups with NACLs? Set broad rules and/or DENY riles and then use security groups for fine grained rules. Ex: deny traffic from specific IP's with NACLs but not with Security Groups.
   * Creating routing table for each of the types of the subnets we can route the traffic depending if we want to make it public or private traffic.
   * An Internet Gateway establishes outside connectivity for EC2 instances that will be deployed into the VPC and provides both inbound and outbound connectivity to workloads running in public subnets whereas a NAT Gateway provides outbound connectivity for workloads running in private subnets. The NAT Gateway is associated to the public subnet and configure the routing of the private subnet to route the outbound traffic through it.
   * VPC Endpoints are private links to supported AWS services from a VPC, instead of reaching the service's public endpoints through the internet. Two types of VPC endpoints exist, Gateway endpoints and Interface endpoints.
   Gateway endpoints support only S3 and DynamoDB, and reach these services through a gateway from the VPC.
   Interface endpoints create a network interface in the VPC's subnets, and all traffic to the service flows through this interface to the service.
   * Since security groups are stateful, you don’t need to edit the outbound rules. The security group will allow the instance to respond to the ping since it saw the ping arrive at the instance. This means that does store the state of the connection creation so if the inbound is allow the response is also allowed.

### Learnings
* EC2 Instance profile is the way to pass IAM role to an EC2 instance. [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

How to create with Cloudformation:

```yaml
# Create the role for the EC2 instance with the required permissions
EC2Role:
  Type: AWS::IAM::Role
  Properties:
    RoleName: "NetworkingWorkshopEC2Role"
    Path: "/"
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      - arn:aws:iam::aws:policy/AmazonS3FullAccess
    AssumeRolePolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Principal:
            Service:
              - ec2.amazonaws.com
          Action:
            - sts:AssumeRole
# Create the instance profile
EC2InstanceProfile:
  Type: AWS::IAM::InstanceProfile
  Properties:
    InstanceProfileName: "NetworkingWorkshopInstanceProfile"
    Path: "/"
    Roles:
      - !Ref EC2Role # Refer the role previously created
```
You can assign the instsance role to the path specific path that contains the role. By default is the `/` But you can use regular expression to match the path. The path is the is the last component of the ARN (resource). Paths can not be created by AWS Management Console, you should use the CLI to manipulate the paths. Examples:

```
arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/Jane
```