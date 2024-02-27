# Bitcoin (BTC) Price v.s. Search Volume
# Challenge: Create the same chart for the Bitcoin Prices vs. Search volumes.
# Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
# Change the y-axis label to 'BTC Price'
# Change the y- and x-axis limits to improve the appearance
# Investigate the linestyles to make the BTC price a dashed line
# Investigate the marker types to make the search datapoints little circles
# Were big increases in searches for Bitcoin accompanied by big increases in the price?
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

years = mdates.YearLocator()
years_fmt = mdates.DateFormatter("%Y")
months = mdates.MonthLocator()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=3, marker='o')

plt.show()

# Unemployement Benefits Search vs. Actual Unemployment in the U.S.
# Challenge Plot the search for "unemployment benefits" against the unemployment rate.
# Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
# Change the y-axis label to: FRED U/E Rate
# Change the axis limits
# Add a grey grid to the chart to better see the years and the U/E rate values. Use dashes for the line style
# Can you discern any seasonality in the searches? Is there a pattern?
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])
df_btc_monthly = df_btc_price.resample("M", on="DATE").mean()

plt.figure(figsize=(14, 9), dpi=120)

plt.title('Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

years = mdates.YearLocator()
years_fmt = mdates.DateFormatter("%Y")
months = mdates.MonthLocator()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim(df_unemployment.index.min(), df_unemployment.index.max())

roll_df = df_unemployment[["UE_BENEFITS_WEB_SEARCH", "UNRATE"]].rolling(window=6).mean()

ax1.grid(color='grey', linestyle='--')

ax1.plot(roll_df.index, roll_df.UNRATE, color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(roll_df.index, roll_df.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3, marker='o')

plt.show()

# Including 2020 in Unemployment Charts
# Challenge: Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame. Convert the MONTH column
# to Pandas Datetime objects and then plot the chart. What do you see?
df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14,8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()
