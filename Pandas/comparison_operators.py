import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# getting rid of one data that is definately not an erroneus data

bridge_height = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 621.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)
df['STD'] = pd.rolling_std(df['meters'], 2)

df_std = df.describe()
print(df_std)

# WHERE
df = df[(df['STD'] < df_std['meters']['std'])]

df.plot()
plt.show()
