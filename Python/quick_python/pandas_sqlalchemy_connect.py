#
#  Access your data in Amazon Redshift and PostgreSQL with Python and R
#  https:\\/www.blendo.co/blog/access-your-data-in-amazon-redshift-and-postgresql-with-python-and-r/?utm_medium=referral&utm_source=quora.com&utm_campaign=connect-to-redshift-using-python
#
#  Plot Data From Amazon Redshift in Python
#  https://plot.ly/python/amazon-redshift/#psycopg2


############ REQUIREMENTS ####################
# sudo apt-get install python-pip
# sudo apt-get install libpq-dev
# sudo pip install psycopg2
# sudo pip install sqlalchemy
# sudo pip install sqlalchemy-redshift
# sudo pip install pandas
##############################################

from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os
from urllib.parse import quote_plus

redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'prod'

# redshift_endpoint = "preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com:5439/prod"
#redshift_endpoint = "preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com"

# engine_str = "redshift+psycopg2://%s:%s@%s:%s/%s" % (redshift_user,redshift_pass,redshift_endpoint,str(port),dbname)

# engine = create_engine(engine_str)

redshift_conn_str = 'redshift+psycopg2://{User}:{Password}@{redshift_endpoint}:{redshift_port}/'\
           '{redshift_dbname}'

redshift_engine = create_engine(redshift_conn_str.format(
    User = redshift_user,
    Password = redshift_pass,
    redshift_endpoint = quote_plus('preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com'),
    redshift_port = quote_plus('5439'),
    redshift_dbname = quote_plus('prod')
    )
                              )


mhx_yearly = pd.read_sql_query('select * from edw.mhx_counts_yearly order by service_year desc;', redshift_engine)

mhx_yearly

mx_data = pd.read_sql_query('select * from edw.mhx_claims limit 50;', redshift_engine)
mx_data
mx_data.count

mx_data.groupby(['payer_plan_type']).count()
mx_data[['payer_plan_type', 'claim_txn_id']].groupby(['payer_plan_type']).count()

########## close session in the end ###############
#s.close()



########## Connect to Athena ##########
import pyathenajdbc
# import pyathena


# awsathena+jdbc://{User}:{Password}@athena.{AwsRegion}.amazonaws.com:443/{Schema}?S3OutputLocation={S3OutputLocation}&driver_path={driver_path}&...

aws_key = os.getenv("AWS_KEY")
aws_secret = os.getenv("AWS_SECRET")

athena_conn_str = 'awsathena+jdbc://{User}:{Password}@athena.{AwsRegion}.amazonaws.com:443/'\
           '{Schema}?S3OutputLocation={S3OutputLocation}&driver_path={driver_path}&jvm_path={jvm_path}'

athena_engine = create_engine(athena_conn_str.format(
    User = quote_plus(''),
    Password = quote_plus(''),
    AwsRegion = 'us-east-1',
    Schema='default',
    S3OutputLocation = quote_plus('s3://preverity-export/sburklund/athena/'),
    driver_path = quote_plus('C:/redshift/AthenaJDBC42.jar'),
    jvm_path = quote_plus('C:/Users/sburklund/sqlworkbench/jre/bin/client/jvm.dll')
    )
                              )

ath_data = pd.read_sql_query('SELECT * FROM metadata.drg_2019_submit_provider limit 20;', athena_engine)

