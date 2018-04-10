"""
Proving corelation within house markets - dta taken from quandl API
"""

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style

style.use('fivethirtyeight')

api_key = open('api_key.txt', 'r').read()


def get_US_states_list():
    # quandl modules have automatic index as date
    # attempts to read all the dataframes on the page as a list
    list_df_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    df_states = list_df_states[0]
    return df_states[1]


def get_from_quandl_api():
    main_df = pd.DataFrame()
    abbv_not_found = []

    # date is a default index from quandl, so it joins on date if not specified on=' '
    # data from Freddie Mac
    for abbv in get_US_states_list():
        query = "FMAC/HPI_{}".format(str(abbv))
        try:
            df = quandl.get(query, authtoken=api_key)
            if main_df.empty:
                main_df = df
                names = [abbv]
            else:
                main_df = pd.merge(main_df, df, left_index=True, right_index=True)
                names.append(abbv)
        except quandl.errors.quandl_error.NotFoundError:
            abbv_not_found.append(abbv)
    main_df.columns = names
    print(abbv_not_found)
    save_to_csv(main_df)


def save_to_csv(df):
    df.to_csv('US_states.csv')


def get_df_from_csv():
    df = pd.read_csv('US_states.csv')
    df.set_index('Date', inplace=True)
    return df


def save_to_bytes(df):
    pickle_out = open('states.pickle', 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()


def get_df_from_pickle():
    pickle_in = open('states.pickle')
    df = pickle.load(pickle_in)
    pickle_in.close()
    return df


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    cur_df = df["United States"]
    df["United States"] = (cur_df - cur_df[0]) / cur_df[0] * 100
    return df["United States"]


def present_data2(df):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    benchmark = HPI_Benchmark()
    df.plot(ax=ax1)
    benchmark.plot(ax=ax1, color='k', linewidth=10)
    plt.legend().remove()
    plt.show()


def present_data(df):
    fig = plt.figure()
    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)
    df[['TX', 'TX12MA']].plot(ax=ax1)
    df[['TX12STD']].plot(ax=ax2)
    plt.show()


def get_correletion(df):
    HPI_State_correlation = df.corr()
    statistics = HPI_State_correlation.describe()
    print(statistics)


def mean_and_std(HPI_data):
    HPI_data.index = pd.to_datetime(HPI_data.index)
    HPI_data['TX12MA'] = HPI_data['TX'].rolling(window=12, center=False).mean()
    HPI_data['TX12STD'] = HPI_data['TX'].rolling(window=12, center=False).std()
    HPI_data.dropna(inplace=True)
    print(HPI_data[['TX', 'TX12MA', 'TX12STD']].head())
    present_data(HPI_data)


if __name__ == '__main__':
    HPI_data = get_df_from_csv()
    mean_and_std(HPI_data)
