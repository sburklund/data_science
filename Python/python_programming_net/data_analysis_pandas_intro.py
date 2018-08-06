import pandas as pd
import datetime
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
#import pandas_datareader.data as web
import pandas_datareader as pdr
#pdr.get_data_yahoo('AAPL')

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()

df = pdr.DataReader('F', 'morningstar', start, end)
#print(df)
