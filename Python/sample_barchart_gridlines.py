import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Using only matplotlib
plt.figure()
plt.bar(range(5), np.random.random(5))
ax=plt.axes()
ax.yaxis.grid()
plt.show(False)

# Using Pandas to plot
df = pd.DataFrame({'B': [5, 10, 6, 8, 4]},
                  index = ['one', 'two', 'three', 'four', 'five'])

print(df)
plt.figure()
subplot = df['B'].plot(kind = 'bar')
subplot.yaxis.grid() # horizontal lines
plt.show()


