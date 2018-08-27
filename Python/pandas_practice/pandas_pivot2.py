# examples worked from
# http://pandas.pydata.org/pandas-docs/stable/reshaping.html

import pandas as pd
import numpy as np 
import datetime

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['A', 'B', 'C'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randn(24),
                   'E': np.random.randn(24),
                   'F': [datetime.datetime(2013, i, 1) for i in range(1, 13)] +
                        [datetime.datetime(2013, i, 15) for i in range(1, 13)]})

#print(df.head())
print(df)

# This is pivoting on A & B and putting the values in C into colums
# It is calculating the mean of column D (defaulting agg func is numpy.mean)
df1 = pd.pivot_table(df, values = 'D', index = ['A', 'B'], columns = ['C'])

print(df1)

df2 = pd.pivot_table(df, values = 'D', index = ['B'], columns = ['A', 'C'], aggfunc = np.sum)
print(df2)



