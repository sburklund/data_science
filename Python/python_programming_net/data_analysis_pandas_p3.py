import pandas as pd

df3 = pd.read_csv('data/HPI_AT_state.csv', names=['state', 'year', 'qtr', 'hpi'])
print(df3.head())

df3.to_html('data/hpi_at_state.html')

df3z = pd.read_csv('data/Zip_Zhvi_3bedroom.csv')
print(df3z.head())
print(list(df3z))
print(df3z.shape)
print(df3z.columns)
# print(df3z.dtypes)
print(df3z.count())

# reshape the data so the year month of the value is in a row instead of 274 columns
df3zz = df3z.melt(id_vars=['RegionID', 'RegionName', 'City', 'State', 'Metro', 'CountyName', 'SizeRank'],
                  var_name='year_month')
# cheese.melt(id_vars=['first', 'last'], var_name='quantity')
print(df3zz.head(10))
print(df3zz.tail(10))
