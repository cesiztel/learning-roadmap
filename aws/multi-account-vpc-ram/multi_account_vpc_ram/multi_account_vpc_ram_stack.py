from aws_cdk import (
    CfnResource,
    CfnTag,
    Fn,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_lambda as lambda_,
)
from constructs import Construct

# Inline source for the IPv6 workaround custom resource Lambda. CloudFormation
# (and MapPublicIpOnLaunch) can't set AssignIpv6AddressOnCreation on a subnet
# at creation time, so this function flips it on after the WEB subnets exist.
IPV6_WORKAROUND_LAMBDA_CODE = """import cfnresponse
import boto3

def lambda_handler(event, context):
    if event['RequestType'] is 'Delete':
      cfnresponse.send(event, context, cfnresponse.SUCCESS)
      return

    responseValue = event['ResourceProperties']['SubnetId']
    ec2 = boto3.client('ec2', region_name='${AWS::Region}')
    ec2.modify_subnet_attribute(AssignIpv6AddressOnCreation={
                                    'Value': True
                                  },
                                  SubnetId=responseValue)
    responseData = {}
    responseData['SubnetId'] = responseValue
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
"""


class MultiAccountVpcRamStack(Stack):
    """Animals4Life base VPC Template v3 - DB, APP and WEB Tiers.

    Direct CDK (Python) translation of template_example.yaml, built with L1
    (Cfn*) constructs so the resulting resource graph mirrors the original
    CloudFormation template one-to-one.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ------------------------------------------------------------------
        # VPC
        # ------------------------------------------------------------------
        vpc = ec2.CfnVPC(
            self, "VPC",
            cidr_block="10.16.0.0/16",
            enable_dns_support=True,
            enable_dns_hostnames=True,
            tags=[CfnTag(key="Name", value="a4l-sharedvpc")],
        )

        ipv6_cidr_block = ec2.CfnVPCCidrBlock(
            self, "IPv6CidrBlock",
            vpc_id=vpc.ref,
            amazon_provided_ipv6_cidr_block=True,
        )

        # ------------------------------------------------------------------
        # Internet Gateway
        # ------------------------------------------------------------------
        internet_gateway = ec2.CfnInternetGateway(
            self, "InternetGateway",
            tags=[CfnTag(key="Name", value="A4L-vpc1-igw")],
        )

        internet_gateway_attachment = ec2.CfnVPCGatewayAttachment(
            self, "InternetGatewayAttachment",
            vpc_id=vpc.ref,
            internet_gateway_id=internet_gateway.ref,
        )

        # ------------------------------------------------------------------
        # WEB route table (public)
        # ------------------------------------------------------------------
        route_table_web = ec2.CfnRouteTable(
            self, "RouteTableWeb",
            vpc_id=vpc.ref,
            tags=[CfnTag(key="Name", value="A4L-vpc1-rt-web")],
        )

        route_table_web_default_ipv4 = ec2.CfnRoute(
            self, "RouteTableWebDefaultIPv4",
            route_table_id=route_table_web.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=internet_gateway.ref,
        )
        route_table_web_default_ipv4.add_dependency(internet_gateway_attachment)

        route_table_web_default_ipv6 = ec2.CfnRoute(
            self, "RouteTableWebDefaultIPv6",
            route_table_id=route_table_web.ref,
            destination_ipv6_cidr_block="::/0",
            gateway_id=internet_gateway.ref,
        )
        route_table_web_default_ipv6.add_dependency(internet_gateway_attachment)

        # ------------------------------------------------------------------
        # Subnets - Reserved / DB / APP (private) and WEB (public)
        # ------------------------------------------------------------------
        def ipv6_subnet_cidr(subnet_part: str) -> str:
            """Derive a /64 IPv6 subnet CIDR from the VPC's auto-assigned /56."""
            vpc_part = Fn.select(
                0, Fn.split("00::/56", Fn.select(0, vpc.attr_ipv6_cidr_blocks))
            )
            return Fn.sub(
                "${VpcPart}${SubnetPart}",
                {"SubnetPart": subnet_part, "VpcPart": vpc_part},
            )

        subnet_reserved_a = ec2.CfnSubnet(
            self, "SubnetReservedA",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(0, Fn.get_azs("")),
            cidr_block="10.16.0.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("00::/64"),
            tags=[CfnTag(key="Name", value="sn-reserved-A")],
        )
        subnet_reserved_a.add_dependency(ipv6_cidr_block)

        subnet_reserved_b = ec2.CfnSubnet(
            self, "SubnetReservedB",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(1, Fn.get_azs("")),
            cidr_block="10.16.64.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("04::/64"),
            tags=[CfnTag(key="Name", value="sn-reserved-B")],
        )
        subnet_reserved_b.add_dependency(ipv6_cidr_block)

        subnet_reserved_c = ec2.CfnSubnet(
            self, "SubnetReservedC",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(2, Fn.get_azs("")),
            cidr_block="10.16.128.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("08::/64"),
            tags=[CfnTag(key="Name", value="sn-reserved-C")],
        )
        subnet_reserved_c.add_dependency(ipv6_cidr_block)

        subnet_db_a = ec2.CfnSubnet(
            self, "SubnetDBA",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(0, Fn.get_azs("")),
            cidr_block="10.16.16.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("01::/64"),
            tags=[CfnTag(key="Name", value="sn-db-A")],
        )
        subnet_db_a.add_dependency(ipv6_cidr_block)

        subnet_db_b = ec2.CfnSubnet(
            self, "SubnetDBB",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(1, Fn.get_azs("")),
            cidr_block="10.16.80.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("05::/64"),
            tags=[CfnTag(key="Name", value="sn-db-B")],
        )
        subnet_db_b.add_dependency(ipv6_cidr_block)

        subnet_db_c = ec2.CfnSubnet(
            self, "SubnetDBC",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(2, Fn.get_azs("")),
            cidr_block="10.16.144.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("09::/64"),
            tags=[CfnTag(key="Name", value="sn-db-C")],
        )
        subnet_db_c.add_dependency(ipv6_cidr_block)

        subnet_app_a = ec2.CfnSubnet(
            self, "SubnetAPPA",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(0, Fn.get_azs("")),
            cidr_block="10.16.32.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("02::/64"),
            tags=[CfnTag(key="Name", value="sn-app-A")],
        )
        subnet_app_a.add_dependency(ipv6_cidr_block)

        subnet_app_b = ec2.CfnSubnet(
            self, "SubnetAPPB",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(1, Fn.get_azs("")),
            cidr_block="10.16.96.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("06::/64"),
            tags=[CfnTag(key="Name", value="sn-app-B")],
        )
        subnet_app_b.add_dependency(ipv6_cidr_block)

        subnet_app_c = ec2.CfnSubnet(
            self, "SubnetAPPC",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(2, Fn.get_azs("")),
            cidr_block="10.16.160.0/20",
            assign_ipv6_address_on_creation=True,
            ipv6_cidr_block=ipv6_subnet_cidr("0A::/64"),
            tags=[CfnTag(key="Name", value="sn-app-C")],
        )
        subnet_app_c.add_dependency(ipv6_cidr_block)

        subnet_web_a = ec2.CfnSubnet(
            self, "SubnetWEBA",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(0, Fn.get_azs("")),
            cidr_block="10.16.48.0/20",
            map_public_ip_on_launch=True,
            ipv6_cidr_block=ipv6_subnet_cidr("03::/64"),
            tags=[CfnTag(key="Name", value="sn-web-A")],
        )
        subnet_web_a.add_dependency(ipv6_cidr_block)

        subnet_web_b = ec2.CfnSubnet(
            self, "SubnetWEBB",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(1, Fn.get_azs("")),
            cidr_block="10.16.112.0/20",
            map_public_ip_on_launch=True,
            ipv6_cidr_block=ipv6_subnet_cidr("07::/64"),
            tags=[CfnTag(key="Name", value="sn-web-B")],
        )
        subnet_web_b.add_dependency(ipv6_cidr_block)

        subnet_web_c = ec2.CfnSubnet(
            self, "SubnetWEBC",
            vpc_id=vpc.ref,
            availability_zone=Fn.select(2, Fn.get_azs("")),
            cidr_block="10.16.176.0/20",
            map_public_ip_on_launch=True,
            ipv6_cidr_block=ipv6_subnet_cidr("0B::/64"),
            tags=[CfnTag(key="Name", value="sn-web-C")],
        )
        subnet_web_c.add_dependency(ipv6_cidr_block)

        # WEB route table associations
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationWebA",
            subnet_id=subnet_web_a.ref,
            route_table_id=route_table_web.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationWebB",
            subnet_id=subnet_web_b.ref,
            route_table_id=route_table_web.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationWebC",
            subnet_id=subnet_web_c.ref,
            route_table_id=route_table_web.ref,
        )

        # ------------------------------------------------------------------
        # IPv6 workaround custom resource (AssignIpv6AddressOnCreation can't
        # be set together with MapPublicIpOnLaunch at subnet creation time)
        # ------------------------------------------------------------------
        ipv6_workaround_role = iam.CfnRole(
            self, "IPv6WorkaroundRole",
            assume_role_policy_document={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"Service": ["lambda.amazonaws.com"]},
                        "Action": ["sts:AssumeRole"],
                    }
                ],
            },
            path="/",
            policies=[
                iam.CfnRole.PolicyProperty(
                    policy_name=Fn.sub("ipv6-fix-logs-${AWS::StackName}"),
                    policy_document={
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": [
                                    "logs:CreateLogGroup",
                                    "logs:CreateLogStream",
                                    "logs:PutLogEvents",
                                ],
                                "Resource": "arn:aws:logs:*:*:*",
                            }
                        ],
                    },
                ),
                iam.CfnRole.PolicyProperty(
                    policy_name=Fn.sub("ipv6-fix-modify-${AWS::StackName}"),
                    policy_document={
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": ["ec2:ModifySubnetAttribute"],
                                "Resource": "*",
                            }
                        ],
                    },
                ),
            ],
        )

        ipv6_workaround_lambda = lambda_.CfnFunction(
            self, "IPv6WorkaroundLambda",
            handler="index.lambda_handler",
            code=lambda_.CfnFunction.CodeProperty(
                zip_file=Fn.sub(IPV6_WORKAROUND_LAMBDA_CODE),
            ),
            runtime="python3.9",
            role=ipv6_workaround_role.attr_arn,
            timeout=30,
        )

        CfnResource(
            self, "IPv6WorkaroundSubnetWEBA",
            type="Custom::SubnetModify",
            properties={
                "ServiceToken": ipv6_workaround_lambda.attr_arn,
                "SubnetId": subnet_web_a.ref,
            },
        )
        CfnResource(
            self, "IPv6WorkaroundSubnetWEBB",
            type="Custom::SubnetModify",
            properties={
                "ServiceToken": ipv6_workaround_lambda.attr_arn,
                "SubnetId": subnet_web_b.ref,
            },
        )
        CfnResource(
            self, "IPv6WorkaroundSubnetWEBC",
            type="Custom::SubnetModify",
            properties={
                "ServiceToken": ipv6_workaround_lambda.attr_arn,
                "SubnetId": subnet_web_c.ref,
            },
        )

        # ------------------------------------------------------------------
        # Default security group
        # ------------------------------------------------------------------
        default_instance_security_group = ec2.CfnSecurityGroup(
            self, "DefaultInstanceSecurityGroup",
            vpc_id=vpc.ref,
            group_description="Enable SSH access via port 22 IPv4 & v6",
            security_group_ingress=[
                ec2.CfnSecurityGroup.IngressProperty(
                    description="Allow SSH IPv4 IN",
                    ip_protocol="tcp",
                    from_port=22,
                    to_port=22,
                    cidr_ip="0.0.0.0/0",
                ),
                ec2.CfnSecurityGroup.IngressProperty(
                    description="Allow HTTP IPv4 IN",
                    ip_protocol="tcp",
                    from_port=80,
                    to_port=80,
                    cidr_ip="0.0.0.0/0",
                ),
                ec2.CfnSecurityGroup.IngressProperty(
                    description="Allow SSH IPv6 IN",
                    ip_protocol="tcp",
                    from_port=22,
                    to_port=22,
                    cidr_ipv6="::/0",
                ),
            ],
        )

        ec2.CfnSecurityGroupIngress(
            self, "DefaultInstanceSecurityGroupSelfReferenceRule",
            group_id=default_instance_security_group.attr_group_id,
            ip_protocol="tcp",
            from_port=0,
            to_port=65535,
            source_security_group_id=default_instance_security_group.attr_group_id,
        )

        # ------------------------------------------------------------------
        # EIPs / NAT Gateways (one per AZ)
        # ------------------------------------------------------------------
        eip_a = ec2.CfnEIP(self, "EIPA", domain="vpc")
        eip_a.add_dependency(internet_gateway_attachment)

        eip_b = ec2.CfnEIP(self, "EIPB", domain="vpc")
        eip_b.add_dependency(internet_gateway_attachment)

        eip_c = ec2.CfnEIP(self, "EIPC", domain="vpc")
        eip_c.add_dependency(internet_gateway_attachment)

        nat_gateway_a = ec2.CfnNatGateway(
            self, "NatGatewayA",
            allocation_id=eip_a.attr_allocation_id,
            subnet_id=subnet_web_a.ref,
        )
        nat_gateway_b = ec2.CfnNatGateway(
            self, "NatGatewayB",
            allocation_id=eip_b.attr_allocation_id,
            subnet_id=subnet_web_b.ref,
        )
        nat_gateway_c = ec2.CfnNatGateway(
            self, "NatGatewayC",
            allocation_id=eip_c.attr_allocation_id,
            subnet_id=subnet_web_c.ref,
        )

        # ------------------------------------------------------------------
        # Private route tables (one per AZ) routed through their NAT Gateway
        # ------------------------------------------------------------------
        route_table_private_a = ec2.CfnRouteTable(
            self, "RouteTablePrivateA",
            vpc_id=vpc.ref,
            tags=[CfnTag(key="Name", value="A4L-vpc1-rt-privateA")],
        )
        route_table_private_b = ec2.CfnRouteTable(
            self, "RouteTablePrivateB",
            vpc_id=vpc.ref,
            tags=[CfnTag(key="Name", value="A4L-vpc1-rt-privateB")],
        )
        route_table_private_c = ec2.CfnRouteTable(
            self, "RouteTablePrivateC",
            vpc_id=vpc.ref,
            tags=[CfnTag(key="Name", value="A4L-vpc1-rt-privateC")],
        )

        ec2.CfnRoute(
            self, "RouteNatGWA",
            route_table_id=route_table_private_a.ref,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=nat_gateway_a.ref,
        )
        ec2.CfnRoute(
            self, "RouteNatGWB",
            route_table_id=route_table_private_b.ref,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=nat_gateway_b.ref,
        )
        ec2.CfnRoute(
            self, "RouteNatGWC",
            route_table_id=route_table_private_c.ref,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=nat_gateway_c.ref,
        )

        # Private route table associations - Reserved / APP / DB subnets
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationReservedA",
            subnet_id=subnet_reserved_a.ref,
            route_table_id=route_table_private_a.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationAppA",
            subnet_id=subnet_app_a.ref,
            route_table_id=route_table_private_a.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationDBA",
            subnet_id=subnet_db_a.ref,
            route_table_id=route_table_private_a.ref,
        )

        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationReservedB",
            subnet_id=subnet_reserved_b.ref,
            route_table_id=route_table_private_b.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationAppB",
            subnet_id=subnet_app_b.ref,
            route_table_id=route_table_private_b.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationDBB",
            subnet_id=subnet_db_b.ref,
            route_table_id=route_table_private_b.ref,
        )

        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationReservedC",
            subnet_id=subnet_reserved_c.ref,
            route_table_id=route_table_private_c.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationAppC",
            subnet_id=subnet_app_c.ref,
            route_table_id=route_table_private_c.ref,
        )
        ec2.CfnSubnetRouteTableAssociation(
            self, "RouteTableAssociationDBC",
            subnet_id=subnet_db_c.ref,
            route_table_id=route_table_private_c.ref,
        )
