import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# Not necessary, I just do this so I do not show my API key.
api_key = open('api_key.txt', 'r').read()


def get_US_states_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    abbv_not_found = []
    main_df = pd.DataFrame()
    names = []
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

    pickle_out = open('fiddy_states3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["United States"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df.rename(columns={'United States': 'US_HPI'}, inplace=True)
    return df


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('1D').mean()
    df = df.resample('M').mean()
    return df


def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"] - df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df = df.resample('M').mean()
    df.rename(columns={'Adjusted Close': 'sp500'}, inplace=True)
    df = df['sp500']
    return df


def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M').mean()
    df.rename(columns={'Value': 'GDP'}, inplace=True)
    df = df['GDP']
    return df


def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"] - df["Unemployment Rate"][0]) / df["Unemployment Rate"][
        0] * 100.0
    df = df.resample('1D').mean()
    df = df.resample('M').mean()
    return df


grab_initial_state_data()
HPI_data = pd.read_pickle('fiddy_states3.pickle')
m30 = mortgage_30y()
sp500 = sp500_data()
gdp = gdp_data()
HPI_Bench = HPI_Benchmark()
unemployment = us_unemployment()
m30.columns = ['M30']
HPI = HPI_Bench.join([m30, sp500, gdp, unemployment])
HPI.dropna(inplace=True)
print(HPI.corr())
