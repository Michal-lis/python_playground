import pandas as pd
import numpy as np

from matplotlib import style

style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [34, 12, 113, 32, 51, 51],
             'Bounce_Rate': [65, 72, 54, 57, 83, 12]}

df = pd.DataFrame(web_stats)

print(type(np.array(df)))
print(df[['Visitors', 'Bounce_Rate']])
print(type(df.Visitors))
print(type(df['Visitors'].tolist()))
