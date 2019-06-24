#
#  Access your data in Amazon Redshift and PostgreSQL with Python and R
#  https://www.blendo.co/blog/access-your-data-in-amazon-redshift-and-postgresql-with-python-and-r/?utm_medium=referral&utm_source=quora.com&utm_campaign=connect-to-redshift-using-python


############ REQUIREMENTS ####################
# sudo apt-get install python-pip 
# sudo apt-get install libpq-dev
# sudo pip install psycopg2
# sudo pip install sqlalchemy
# sudo pip install sqlalchemy-redshift
# sudo pip install pandas
##############################################

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
import os
import pprint as pretty


from sqlalchemy import create_engine
import psycopg2
import pandas as padas
import os

redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'prod'

engine = "redshift+psycopg2://%s:%s@%s:%s/%s" % (redshift_user,redshift_pass,redshift_endpoint,str(port),dbname)
data_frame = padas.read_sql_query('SELECT * FROM sburklund.nucc_compare;', engine)

