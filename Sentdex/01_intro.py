import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "morningstar", start, end)

print(df)

print(df.head())

df['High'].plot()

plt.legend()
plt.show()

