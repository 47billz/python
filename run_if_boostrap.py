#!/usr/bin/python

import sys
import json
import os
import time
import logging
from urllib import URLopener
import subprocess

def copy_jar_when_ready(source,destination,check):
    logging.warn('startin process {} in master'.format(os.getpid()))
    while not os.path.isfile(check):
        logging.warn('waiting for file to exist ...')
        time.sleep(10)
    download_file(source,destination)

def download_file(source,destination):
    logging.warn('Downloading file ...')
    subprocess.call(['sudo','wget',source,'-P',destination])

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
    #init vars jar_source = sys.argv[1], jar_destination = sys.argv[2] ,
    #check = sys.argv[3]
    jar_source = 'http://central.maven.org/maven2/com/google/guava/guava/25.1-jre/guava-25.1-jre.jar'
    jar_destination = '/usr/lib/spark/jars/'
    instance_info = "/mnt/var/lib/info/instance.json"
    check = '/var/run/spark/spark-history-server.pid'
    
    if is_master(instance_info):
        pid = os.fork()
        try:
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            logging.error("Failed to Demonize: %d, %s\n" % (e.errno,e.strerror))
            sys.exit(1)
        
        os.setsid()
        pid = os.fork()
        try:
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            logging.error("Failed to Demonize: %d, %s\n" % (e.errno,e.strerror))
            sys.exit(1)
        copy_jar_when_ready(jar_source,jar_destination,check)
    else:
        logging.warn('instance is not mastser, exiting ..')
        sys.exit(0)