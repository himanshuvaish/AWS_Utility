import boto3
client = boto3.resource('ec2',region_name='eu-west-1')

def applytag(myinstanceid):
    ### assign tag
    instance = client.Instance(myinstanceid)

    tag = instance.create_tags(Tags=[
            { 'Key': 'START', 'Value': '07:55' },
            { 'Key': 'START_DAYS', 'Value': 'Mo,Tu,We,Th,Fr' },
            { 'Key': 'STOP', 'Value': '19:55' },
            { 'Key': 'STOP_DAYS', 'Value': 'Mo,Tu,We,Th,Fr' },
            { 'Key': 'Creator', 'Value': 'Giuseppe Borgese' },
            { 'Key': 'Request from', 'Value': 'my dear colleague' },
            { 'Key': 'Team', 'Value': 'developer and testers' }
        ]
    )
    print tag

applytag('i-xxxxxxxxxxx')
