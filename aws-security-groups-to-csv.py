import boto3
import csv
from pprint import pprint

ec2 = boto3.client('ec2')
response = ec2.describe_security_groups()

with open('firewall_rules.csv', 'wb') as csv:
    for security_group in response['SecurityGroups']:
        description = security_group['Description']
        id = security_group['GroupId']
        group_name = security_group['GroupName']
        vpc_id = security_group['VpcId']
        for permission in security_group['IpPermissions']:
            if 'FromPort' in permission:
                from_port = permission['FromPort']
                proto = permission['IpProtocol']
                
                for ip_range in permission['IpRanges']:
                    range_description = ''
                    if 'Description' in ip_range:
                        range_description = ip_range['Description']
                    ip_range = ip_range['CidrIp']
                    rule = ip_range + ',' + str(from_port) + ',' + str(proto) + ',' + range_description + ',' + group_name + ',' +id + ',' + vpc_id
                    csv.write(rule)
                    csv.write('\n')
                    print(rule)
                
            