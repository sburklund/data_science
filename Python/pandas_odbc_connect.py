#  Access your data in Amazon Redshift and PostgreSQL with Python and R
#  https:\\/www.blendo.co/blog/access-your-data-in-amazon-redshift-and-postgresql-with-python-and-r/?utm_medium=referral&utm_source=quora.com&utm_campaign=connect-to-redshift-using-python
#
#  Plot Data From Amazon Redshift in Python
#  https://plot.ly/python/amazon-redshift/#psycopg2
#
# Redshift ODBC documantaion
# https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.27.1000/Amazon+Redshift+ODBC+Driver+Install+Guide.pdf


############ REQUIREMENTS ####################
# sudo apt-get install python-pip
# sudo apt-get install libpq-dev
# sudo pip install psycopg2
# sudo pip install sqlalchemy
# sudo pip install sqlalchemy-redshift
# sudo pip install pandas
# sudo pip install pyodbc
##############################################

# from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import pyodbc
import os
from urllib.parse import quote_plus

redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")

# redshift_endpoint = "preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com:5439/prod"
# redshift_endpoint = "preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com"
# ODBC URL = Driver={Amazon Redshift (x64)}; Server=preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com; Database=prod

# DNS connection is prefered because it encrypts the user/password.  DNS-less does NOT
redshift_odbc_dsn = pyodbc.connect("DSN=Amazon_Redshift_ODBC_DSN")  # Note - cannot have spaces before/after equal sign


# DNS-less connection.  This could expose user/password in clear text
redshift_odbc_dsnless = pyodbc.connect("Driver={Amazon Redshift (x64)};"
                                       "Server=preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com;"
                                       "Port=5439;"
                                       "Database=prod;"
                                       f"uid={redshift_user};pwd={redshift_pass}"
                                       )


mhx_yearly= pd.read_sql_query('select * from edw.mhx_counts_yearly order by service_year desc;', redshift_odbc_dsn)
mhx_yearly.sort_values(['service_year'])

mhx_yearly2 = pd.read_sql_query('select * from edw.mhx_counts_yearly order by service_year desc;', redshift_odbc_dsnless)
mhx_yearly2.sort_values(['mhx_claim_lines'])