"""
Proving corelation within house markets - dta taken from quandl API
"""

import quandl
import pandas as pd
import pickle

api_key = open('api_key.txt', 'r').read()


def get_US_states_list():
    # quandlmodules have automatic index as date
    # attempts to read all the dataframes on the page as a list
    list_df_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    df_states = list_df_states[0]
    return df_states[1]


def get_from_quandl_api():
    main_df = pd.DataFrame()
    abbv_not_found = []

    # date is a default index from quandl, so it joins on date if not specified on=' '

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


if __name__ == '__main__':
    df_HPI = get_df_from_csv()
    print(df_HPI.head())
