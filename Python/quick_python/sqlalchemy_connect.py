# source website
# https://gist.github.com/varver/f6f1ad1a1cfd786f8e374d11fd3dbd4b

############ REQUIREMENTS ####################
# sudo apt-get install python-pip 
# sudo apt-get install libpq-dev
# sudo pip install psycopg2
# sudo pip install sqlalchemy
# sudo pip install sqlalchemy-redshift
##############################################

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
import os
import pprint as pretty

redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'prod'
SCHEMA = "sburklund"      #default is "public" 

#>>>>>>>> MAKE CHANGES HERE <<<<<<<<<<<<< 
DATABASE = "dbname"
USER = "username"
PASSWORD = "password"
HOST = "host"
PORT = "port"
SCHEMA = "sburklund"      #default is "public" 

####### connection and session creation ############## 
connection_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (redshift_user,redshift_pass,redshift_endpoint,str(port),dbname)
engine = sa.create_engine(connection_string)
session = sessionmaker()
session.configure(bind=engine)
s = session()
SetPath = "SET search_path TO %s" % SCHEMA
s.execute(SetPath)
###### All Set Session created using provided schema  #######

################ write queries from here ###################### 
query = "select * from sburklund.nucc_compare;"
rr = s.execute(query)
all_results =  rr.fetchall()

def pretty(all_results):
    for row in all_results :
        print("row start >>>>>>>>>>>>>>>>>>>>")
        for r in row :
            print(" ----" , r)
            print("row end >>>>>>>>>>>>>>>>>>>>>>")

pretty(all_results)

print(all_results)

########## close session in the end ###############
s.close()