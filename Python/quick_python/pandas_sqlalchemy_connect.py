#
#  Access your data in Amazon Redshift and PostgreSQL with Python and R
#  https://www.blendo.co/blog/access-your-data-in-amazon-redshift-and-postgresql-with-python-and-r/?utm_medium=referral&utm_source=quora.com&utm_campaign=connect-to-redshift-using-python
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

redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'prod'

engine_str = "redshift+psycopg2://%s:%s@%s:%s/%s" % (redshift_user,redshift_pass,redshift_endpoint,str(port),dbname)

engine = create_engine(engine_str)
data_frame = pd.read_sql_query('SELECT * FROM sburklund.nucc_compare;', engine)

data_frame

mx_data = pd.read_sql_query('select * from edw.mhx_claims limit 50;', engine)
mx_data
mx_data.count

mx_data.groupby(['payer_plan_type']).count()
mx_data[['payer_plan_type', 'claim_txn_id']].groupby(['payer_plan_type']).count()

########## close session in the end ###############
s.close()
