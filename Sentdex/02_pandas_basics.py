import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

#df.set_index('Day')

#df = df.set_index('Day')

df.set_index('Day', inplace = True)

#Two methods of printing a column
print(df['Visitors'])
print(df.Visitors)

#Printing multiple columns
print(df[['Bounce Rate', 'Visitors']])

#Converting column output to a list
print(df.Visitors.tolist())
print(df['Visitors'].tolist())

#Converting column output to an array
print(np.array(df[['Bounce Rate', 'Visitors']]))

#Converting our newly formed array into a pandas dataframe
df2 = pd.DataFrame(np.array(df[['Bounce Rate', 'Visitors']]))

print(df)
print(df.tail())
print(df.head(2))
