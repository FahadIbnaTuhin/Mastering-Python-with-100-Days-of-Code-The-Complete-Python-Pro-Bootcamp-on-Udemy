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

# Challenge: Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes. Label
# one axis 'TSLA Stock Price' and the other 'Search Trend'.

import pandas as pd
import matplotlib.pyplot as plt

df_tesla = pd.read_csv("TESLA Search Trend vs Price.csv")

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Tesla Stock Price', color='#E6232E')
ax2.set_ylabel('Search Trend', color='skyblue')

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

# Challenge: Make the chart larger and easier to read.
#
# Increase the figure size (e.g., to 14 by 8).
# Increase the font sizes for the labels and the ticks on the x-axis to 14.
# Rotate the text on the x-axis by 45 degrees.
# Make the lines on the chart thicker.
# Add a title that reads 'Tesla Web Search vs Price'
# Keep the chart looking sharp by changing the dots-per-inch or DPI value.
# Set minimum and maximum values for the y and x axis. Hint: check out methods like set_xlim().
# Finally use plt.show() to display the chart below the cell instead of relying on the automatic notebook output.
plt.figure(figsize=(14, 8), dpi=120)
# In this case, you've set the dpi to 120, which means there are 120 dots (or pixels) per inch. Increasing the dpi will
# result in a higher resolution image but may also increase the file size.
ax1 = plt.gca()
ax2 = ax1.twinx()

plt.title("Price vs Search Trend")

ax1.set_ylabel('Price', fontsize=14, color='#E6232E')
ax2.set_ylabel('Search Trend', fontsize=14, color='skyblue')

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, linewidth=3, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, linewidth=3, color='skyblue')

plt.show()

# Increase the size and rotate the labels on the x-axis
# plt.xticks(fontsize=14, rotation=45)

# Here's the code with rotation added to the x-ticks. With .set_ylim() and .set_xlim() you have precise control over
# which data you want to show on the chart. You can either choose hard values like displaying the Tesla stock price
# between $0 and $600. Or you could use the .min() and .max() functions to help you work out the bounds for the chart
# as well.
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# Adding Locator Tick Marks. The first step is importing matplotlib.dates.  This is where all the date plotting
# capabilities live.
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# Next, we need a YearLocator() and a MonthLocator() objects, which will help Matplotlib find the years and the months.
# Then we also need a DateFormatter(), which will help us specify how we want to display the dates.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Bitcoin (BTC) Price v.s. Search Volume
# Challenge: Create the same chart for the Bitcoin Prices vs. Search volumes.
#
# Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
# Change the y-axis label to 'BTC Price'
# Change the y- and x-axis limits to improve the appearance
# Investigate the linestyles to make the BTC price a dashed line
# Investigate the marker types to make the search datapoints little circles
# Were big increases in searches for Bitcoin accompanied by big increases in the price?

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')

df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])
df_btc_monthly = df_btc_price.resample("M", on="DATE").mean()

plt.figure(figsize=(14, 9), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
	color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
	color='skyblue', linewidth=3, marker='o')

plt.show()














