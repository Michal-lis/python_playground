import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style

style.use('fivethirtyeight')

api_key = open('api_key.txt', 'r').read()


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start='1975-01-01', authtoken=api_key)
    cur_df = df["Value"]
    cur_df = (cur_df - cur_df[0]) / cur_df[0] * 100
    save_to_csv(cur_df)
    return cur_df


def save_to_csv(df):
    df.to_csv('30y_Martgage.csv')


if __name__ == '__main__':
    # df = mortgage_30y()
    df = pd.read_csv('30y_Martgage.csv')
    print(df)
