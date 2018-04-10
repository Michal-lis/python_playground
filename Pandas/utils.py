import pandas as pd

df1 = pd.DataFrame({'HPI': [80, 83, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 83, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])


def concat_append():
    # concatenating dataframes
    # populating NaN where the data is missing
    concat = pd.concat([df1, df2, df3])

    # appending
    df4 = df1.append(df2).append(df3)
    s = pd.Series([800, 2, 50], index=['HPI', 'Int_rate', 'US_GDP_Thousands'])
    # ignore index automatically adds the next index
    df4 = df4.append(s, ignore_index=True)
    print(df4)


def merge():
    # merge ignores index
    # merging creates a new columns on duplicated data
    df5 = pd.merge(df1, df2, on=['HPI', 'Int_rate'])
    print(df5)


def join():
    # joins on index on default
    # df1.set_index('HPI', inplace=True)
    # df3.set_index('HPI', inplace=True)
    joined = df1.join(df3, lsuffix='_left', rsuffix='_right')
    print(joined)


if __name__ == '__main__':
    print(df1)
    print(df2)
    print(df3)
    join()
