import pandas as pd

df = pd.read_csv("003 salaries-by-college-major.csv")

clean_df = df.dropna()
# print(clean_df.tail())

# print(clean_df.groupby("Group").count())
print(clean_df.groupby("Group").mean())

pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby("Group").mean())

# Work with recent data: https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors
