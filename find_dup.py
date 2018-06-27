"""
Description:	This program finds duplicates of files in a specified or current
				directory

Input:			Either a file path or nothing(in the case of current directory)
Output:			A log file named log.txt

How to run: In the command line, one has to type 'python find_dup_v1.1.py'
			followed by the file path (seperated by one space).
			The log file 'log.txt' will be outputted in the same directory where
			find_dup_v1.1.py is.

Author: Mfundo Bill
latest update: 17:56 17/05/2016
"""
import sys
import time
import glob
import os

def read_file(file_name):
	"""inputs a file name/path and returns the content of a file as a string"""
	File = open(file_name,'r')
	return File.read()

"""Accepts a string and returns it's hash"""
def get_hash(string):
        return hash(string)

def found_in(key,Table):
	""" Accepts a key(string) and a table(dict) and returns a boolean (True/False)"""
	return key in Table

def find_duplicates(file_list,Table,log,number_of_duplicates):
	""" Accepts a file list, table, log, number_of_duplicates and returns a
	 	2-tuple (log,number_of_duplicates)
		This is the main algorithm for finding duplicates, it implements a hash
		table and looks for collisions as the duplicates"""
	for file_name in file_list:
		file_content = read_file(file_name)
		file_hash = get_hash(file_content)
		if found_in(file_hash,Table):
			log = log + os.path.basename(file_name)+' is duplicate to '+Table[file_hash]+'\n'
			number_of_duplicates = number_of_duplicates + 1
		else:
			Table[file_hash] = os.path.basename(file_name)
	return log,number_of_duplicates

"""This is where we take care of what comes in to the commandline"""
if len(sys.argv)>1:
	directory = sys.argv[1] #The first argument after the name of the program
	file_list = glob.glob(directory+'*.pdf') #glob outputs an array of file names in directory
else:
	file_list = glob.glob('*.dat')

Table = {} #creating an empty hash table
number_of_duplicates = 0
"""We sort the list for the order at which the duplicates will be written in the
	log file"""
file_list.sort()

"""The following line logs the current time and and date on the system"""
log = time.strftime("%d/%m/%Y")+' '+time.strftime("%H:%M:%S")+'\n'

log,number_of_duplicates = find_duplicates(file_list,Table,log,number_of_duplicates)

"""The following block of code checks to see if there is anyhing in the log and
	logs the relevant information"""
if len(file_list) == 0:
	log = log + 'No files found\n' #when there is no files in director or a wrong file path has been entered
elif number_of_duplicates == 0:
        log = log +'No duplicates found\n'	#When there are no duplicates found
log_file = open('log.txt','a')
log_file.write(log+'\n')
log_file.close()
