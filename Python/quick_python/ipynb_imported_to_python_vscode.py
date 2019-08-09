#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Python\\quick_python'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ### Import libraries and set up Redshift connnection string

#%%
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os


#%%
redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'prod'

engine_str = "redshift+psycopg2://%s:%s@%s:%s/%s" % (redshift_user,redshift_pass,redshift_endpoint,str(port),dbname)

engine = create_engine(engine_str)

#%% [markdown]
# ### Pull sample data from Redshift into a Pandas dataframe
# show the first 5 rows of the data

#%%
mx_data = pd.read_sql_query('select * from edw.mhx_claims limit 100;', engine)
mx_data.head()

#%% [markdown]
# ### Group data by payer_plan_type with counts of rows

#%%
mx_data.groupby(['payer_plan_type']).count()

#%% [markdown]
# ### Group data by payer_plan_type with counts of rows on 1 column

#%%
mx_data[['payer_plan_type', 'claim_txn_id']].groupby(['payer_plan_type']).count()


#%%
# ### List claim_txn_id
print(mx_data[['claim_txn_id']])

#%% [markdown]
# ### Use Plotly for creating graphics
# #### Note: As of 7/20/2019 need to use plotly.offline instead of plotly.plotly

#%%
#from __future__ import print_function #python 3 support

import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
#import requests

#%% 

mx_ppt = mx_data[['payer_plan_type', 'claim_txn_id']].groupby(['payer_plan_type']).count()
mx_ppt
mx_ppt.columns

layout = go.Layout(title="Payer Plan Type", yaxis=dict(title="Count"))
data = [go.Bar(x=mx_ppt.index, y=mx_ppt.claim_txn_id)]
py.iplot(go.Figure(data=data, layout=layout))


#%%
