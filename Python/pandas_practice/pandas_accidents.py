# source data
# https://realpython.com/working-with-large-excel-files-in-pandas/
# https://github.com/shantnu/PandasLargeFiles 

import pandas as pd

# Read the file 
data = pd.read_csv("Python/pandas_practice/data/Accidents7904.csv", low_memory= False) 

# Output the number of rows
print("Total rows: {0}".format(len(data))) 

# See which headers ae available 
print(list(data)) 
