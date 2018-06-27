from fabric.api import *
import commands
import boto3

def get_hosts_from_api(cluster_id):
    ''' Get hosts outside cluster for all nodes with public DN '''
    client = boto3.client('emr')
    host_list = []
    response = client.list_instances(
        ClusterId=cluster_id,
        InstanceGroupTypes=[
            'MASTER','CORE',
        ],
    )
    for instance in response['Instances']:
        host_list.append("hadoop@"+instance['PublicDnsName'])
    return host_list

env.hosts = get_hosts_from_api('j-2FIKMPJMPY2A0')
env.key_filename = '~/NewKey.pem'
env.output_prefix = False


def file_get(remotepath, localpath):
    get(remotepath,localpath+"/"+env.host+"/")

@parallel
def cmd(command):
    sudo(command)

@parallel
def edit_conf():
    pass