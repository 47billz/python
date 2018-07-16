#!/usr/bin/python

import sys
import json
import os
import time
import logging
from urllib import URLopener
from multiprocessing import Process

def copy_jar_when_ready(source,destination,name,check):
    logging.warn('startin process {} in master'.format(os.getpid()))
    while not os.path.isfile(check):
        logging.warn('waiting for file to exist ...')
        time.sleep(10)
    results = download_file(source,destination+name)
    logging.warn('{}'.format(results))

def download_file(source,destination):
    logging.warn('Downloading file ...')
    url_opener = URLopener()
    return url_opener.retrieve(source,destination)

def is_master(instance_info):
    is_master = False
    try:
        with open(instance_info) as f:
            instance_info_dict = json.load(f)
        #get instance info
        is_master = instance_info_dict.get('isMaster')
    except IOError as e:
        print(e)
    
    return is_master


if __name__=="__main__":
    #init vars
    jar_source = 'http://central.maven.org/maven2/com/google/guava/guava/25.1-jre/guava-25.1-jre.jar'
    jar_name = jar_source.split('/')[-1]
    jar_destination = './temp/' #'/usr/lib/spark/jars/'
    instance_info = "/mnt/var/lib/info/instance.json"
    check = '/var/run/spark/spark-history-server.pid'
    
    if is_master(instance_info):
        #p = Process(target=copy_jar_when_ready, args=(jar_source,jar_destination,jar_name,check))
        #p.start()
        pid = os.fork()
        if pid == 0:
            copy_jar_when_ready(jar_source,jar_destination,jar_name,check)
        print('bootstrap done')
        sys.exit(0)
    else:
        logging.warn('instance is not mastser, exiting ..')
        sys.exit(0)