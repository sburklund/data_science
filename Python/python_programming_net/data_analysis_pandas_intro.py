import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

## fix for bug in pandas_datareader 0.60.0 https://stackoverflow.com/questions/50394873/import-pandas-datareader-gives-importerror-cannot-import-name-is-list-like
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

# import pandas_datareader as pdr
# pdr.get_data_yahoo('AAPL')

start = datetime.datetime(2017, 6, 1)
# end = datetime.datetime(2018, 1, 1)
end = datetime.datetime.now()
   
df = web.DataReader("F", data_source="iex", start=start,end= end)
df.head(15)
print(df.head())

df.to_csv('data/f_ohlc.csv', sep=',')

df['high'].plot()
plt.legend()
#plt.show()

df['open'].plot()
plt.legend()
plt.show()

# Showing multiple figures without closing the first figure
# https://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib
f1 = plt.figure(1)
df['high'].plot()
plt.legend()

f2 = plt.figure(2)
df['open'].plot()
plt.legend()

plt.show()