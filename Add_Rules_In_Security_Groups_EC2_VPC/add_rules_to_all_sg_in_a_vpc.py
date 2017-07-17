import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

myvpc='vpc-xxxxx'
tcpicmpudprange=[
    {
        'FromPort': 0,
        'IpProtocol': 'udp',
        'IpRanges': [ { 'CidrIp': '172.20.0.0/16' }],
        'ToPort': 65535,
    },
    {
        'FromPort': 0,
        'IpProtocol': 'tcp',
        'IpRanges': [ { 'CidrIp': '172.20.0.0/16' }],
        'ToPort': 65535,
    },
    {
        'FromPort': -1,
        'IpProtocol': 'icmp',
        'IpRanges': [ { 'CidrIp': '172.20.0.0/16' }],
        'ToPort': -1,
    },
        {
            'FromPort': 0,
            'IpProtocol': 'udp',
            'IpRanges': [ { 'CidrIp': '172.21.0.0/16' }],
            'ToPort': 65535,
        },
        {
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [ { 'CidrIp': '172.21.0.0/16' }],
            'ToPort': 65535,
        },
        {
            'FromPort': -1,
            'IpProtocol': 'icmp',
            'IpRanges': [ { 'CidrIp': '172.21.0.0/16' }],
            'ToPort': -1,
        }
]


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    logger.info("Lets start")
    response = client.describe_security_groups(
        Filters=[
            {
                'Name': 'vpc-id',
                'Values': [
                    myvpc,
                ]
            },
        ],)

    for sg in response['SecurityGroups']:
        logger.info(sg['GroupId'])
        security_group = ec2.SecurityGroup(sg['GroupId'])
        response1 = security_group.authorize_egress(IpPermissions=tcpicmpudprange)
        response2 = security_group.authorize_ingress(IpPermissions=tcpicmpudprange)
        logger.info(response1)
        logger.info(response2)


    return 'completed'
