import pandas as pd

df = pd.read_csv("003 salaries-by-college-major.csv")

# print(df)

# Top 5 Rows
# print(df.head())

# To get rows and columns
# print(df.shape)

# print(df.columns)

#  Use the .isna() method and see if you can spot if there's a problem somewhere.
# print(df.isna())

# Check the last couple of rows in the dataframe:
# print(df.tail())

# To delete this any Null
clean_df = df.dropna()
# print(clean_df.tail())

# print(clean_df)
# To access a particular column
# print(clean_df["Starting Median Salary"])


# ------------------------------------Together -----------------------------------------
# To find the highest starting salary we can simply chain the .max() method.
print(clean_df["Starting Median Salary"].max())

# the .idxmax() method will give us index for the row with the largest value.
print(clean_df["Starting Median Salary"].idxmax())

# To see the name of the major that corresponds to that particular row, we can use the .loc (location) property.
print(clean_df["Undergraduate Major"].loc[43])
# To do the same thing:
print(clean_df['Undergraduate Major'][43])

# If you don't specify a particular column you can use the .loc property to retrieve an entire row:
print(clean_df.loc[43])
# Cann't do this with this:
# print(clean_df[43])
# ------------------------------------End-----------------------------------------


# Now that we've found the major with the highest starting salary, can you write the code to find the following:
# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
# print(clean_df["Mid-Career Median Salary"].idxmax())
# print(clean_df["Undergraduate Major"].loc[8])
# print(clean_df.loc[8])

# Which college major has the lowest starting salary and how much do graduates earn after university?
# print(clean_df["Starting Median Salary"].min())

# print(clean_df["Starting Median Salary"].idxmin())
# print(clean_df["Undergraduate Major"].loc[49])
# Converting the above 2 line in 1 line
# print(clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()])

# print(clean_df.loc[clean_df["Starting Median Salary"].idxmin()])

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
print(clean_df["Mid-Career Median Salary"].idxmin())
print(clean_df["Undergraduate Major"].loc[18])
print(clean_df.loc[18])


# Sadly, education is actually the degree with the lowest mid-career salary and Spanish is the major with the lowest starting salary.
