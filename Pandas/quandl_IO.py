import pandas as pd

df = pd.read_csv('ZILLOW-M530_ZHVIBTY.csv')
df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

df2 = pd.read_csv('newcsv2.csv')
print(df2.head())
# csv does not have an index, only normal columns
df2 = pd.read_csv('newcsv2.csv', index_col=0)

# renaming columns
df2.columns = ['Warsaw HPI']
# df._count_level(index is not a column)
print(df2.head())
df2.to_json('newcsv3.json')

df_json = pd.read_json('newcsv3.json')
df_json.rename()
print(df_json.head())
