import boto3
from botocore.exceptions import ClientError
from multiprocessing.dummy import Pool as ThreadPool
import sys,random,time
import csv,jsonpi
import logging

def upload_to_s3(i):
    num_rows = int(sys.argv[2])
    num_columns = int(sys.argv[3])
    bucket = sys.argv[4]
    key =  sys.argv[5]
    
    if len(sys.argv)==7:
        data = json.dumps(columns_json(num_columns,num_rows), indent=2)
        file_extention = '.json'
    else:
        data = generate_column(num_columns,num_rows)
        file_extention = '.csv'

    try:
        s3.put_object(
            Body=data,
            Bucket=bucket,
            Key="A={}/B={}/{}-{}.{}"
                .format(i,str(time.time()+i),key,
                        random.randint(0,9),
                        file_extention)
        )
    except ClientError as e:
        print(e)

def generate_row(num_columns):
    row = ''.join(['{},'.format(random.randint(0,9)) 
                    for i in range(num_columns)])
    return row[:-1]+'\n'

def generate_column(num_rows,num_columns):
    columns = ''.join([generate_row(num_columns) 
                    for i in range(num_rows)])
    print(columns)
    return columns

def rows_json(num_colums):
    result = {}
    for i in range(num_colums):
        result['_{}{}'.format(i,time.clock())]= str(random.randint(0,9))
    return result

def columns_json(num_colums,num_rows):
    result = {}
    for i in range(num_rows):
         result["_"+str(i)]= rows_json(num_colums)
    print(json.dumps(result,indent=2))
    return result

def init_logging():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("botocore")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

if __name__ == "__main__":
    if len(sys.argv)==6 or len(sys.argv)==7 :
        ts = time.clock()
        #init_logging()
        session = boto3.session.Session()
        s3 = session.client('s3')
        pool = ThreadPool(200)
        results = pool.map(upload_to_s3,range(int(sys.argv[1])))
        te = time.clock()
        print("took {} seconds".format(str(te-ts)))
    else:
        print('''Oh my, we need 6 args and you have {}:
python data_gen.py file_count row column bucket prefix
        '''.format(len(sys.argv)))