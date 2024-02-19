import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

# What are the shapes of the dataframes? How many rows and columns? What are the column names?
# df_tesla.shape
# df_tesla["TSLA_WEB_SEARCH"].max()
# df_tesla["TSLA_WEB_SEARCH"].min()

# If you use df_tesla.describe(), you get a whole bunch of descriptive statistics. Right off the bat.
df_tesla.describe()

# What is the periodicity of the time series data (daily, weekly, monthly)?
print(df_tesla["MONTH"].min(), df_tesla["MONTH"].max())

# Solution for Unemployment
# df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
# df_unemployment.shape
# df_unemployment.head()
# print('Largest value for "Unemployemnt Benefits" '
#       f'in Web Search: {df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()}')

# Solution for Bitcoin
# df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
# df_btc_price.shape
# df_btc_price.head()

# df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
# df_btc_search.shape
# df_btc_search.head()

# print(f'largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

# Check for Missing Values
# Challenge: Are there any missing values in any of the dataframes? If so, which row/rows have missing values? How many
# missing values are there?
# df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
# df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
# df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
# df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')

print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')
print(f'Number of missing values: {df_btc_price.isna().values.sum()}')

# Remove any missing values that you found
df_btc_price.dropna(inplace=True)
df_btc_price.isna().values.any()

# Convert Strings to DateTime Objects
# Challenge: Check the data type of the entries in the DataFrame MONTH or DATE columns. Convert any strings in to
# Datetime objects. Do this for all 4 DataFrames. Double check if your type conversion was successful.
# df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
# df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
# df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
# df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

# # print(type(df_tesla["MONTH"].loc[0]))
# df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
# # print(type(df_tesla["MONTH"].loc[0]))
# df_tesla.head()

# df_btc_search["MONTH"] = pd.to_datetime(df_btc_search["MONTH"])
# df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])
# df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])

# Resampling Time Series Data
# Next, we have to think about how to make our Bitcoin price and our Bitcoin search volume comparable. Our Bitcoin price
# is daily data, but our Bitcoin Search Popularity is monthly data.
# To convert our daily data into monthly data, we're going to use the .resample() function. The only things we need to
# specify is which column to use (i.e., our DATE column) and what kind of sample frequency we want (i.e., the "rule").
# We want a monthly frequency, so we use 'M'.  If you ever need to resample a time series to a different frequency, you
# can find a list of different options here (for example 'Y' for yearly or 'T' for minute).

# After resampling, we need to figure out how the data should be treated. In our case, we want the last available price
# of the month - the price at month-end.
# df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

# If we wanted the average price over the course of the month, we could use something like:
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()

