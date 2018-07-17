#!/usr/bin/python

import sys
import json
import os
import time
import logging
import subprocess

def copy_jar_when_ready(source,destination,check):
    '''copy jar when pre-condition is met'''
    logging.warn('startin process {} in master'.format(os.getpid()))
    while not os.path.isfile(check):
        logging.warn('waiting for file to exist ...')
        time.sleep(5)
    download_file(source,destination)

def download_file(source,destination):
    logging.warn('Downloading file ...')
    subprocess.call(['sudo','wget',source,'-P',destination])

def is_master(instance_info):
    '''check if instance is master'''
    is_master = False
    try:
        with open(instance_info) as f:
            instance_info_dict = json.load(f)
        is_master = instance_info_dict.get('isMaster')
    except IOError as e:
        print(e)
    return is_master

def daemonize_proc():
    '''run a new process in the background'''
    pid = os.fork()
    try:
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        logging.error("Failed to Demonize: %d, %s\n" % (e.errno,e.strerror))
        sys.exit(1)


if __name__=="__main__":
    jar_source = 'http://central.maven.org/maven2/com/google/guava/guava/25.1-jre/guava-25.1-jre.jar'
    jar_destination = '/usr/lib/spark/jars/'
    instance_info = "/mnt/var/lib/info/instance.json"
    check = '/var/run/spark/spark-history-server.pid'
    
    if is_master(instance_info):
        daemonize_proc()
        os.setsid()
        daemonize_proc()
        copy_jar_when_ready(jar_source,jar_destination,check)
    else:
        logging.warn('instance is not master, exiting ..')
        sys.exit(0)