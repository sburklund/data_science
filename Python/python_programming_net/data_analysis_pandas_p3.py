import pandas as pd

df3 = pd.read_csv('data/HPI_AT_state.csv', names= ['state', 'year', 'qtr', 'hpi'])
print(df3.head())

df3.to_html('data/hpi_at_state.html')
