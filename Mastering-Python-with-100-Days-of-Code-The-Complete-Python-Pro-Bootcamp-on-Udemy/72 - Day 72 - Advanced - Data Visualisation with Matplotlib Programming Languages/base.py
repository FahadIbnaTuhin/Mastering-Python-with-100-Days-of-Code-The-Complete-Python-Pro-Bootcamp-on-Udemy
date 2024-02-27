import pandas as pd

# Setting the header row to 0 allows us to substitute our own column names.
df = pd.read_csv("002 QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
# print(df.shape)

# To count the number of entries in each column we can use .count(). Note that .count() will actually tell us the number
# of non-NaN values in each column.
# print(df.count())

# If we .sum() the number of posts then we can see how many posts each programming language had since the creation of
# Stack Overflow.
# print(df.groupby("TAG").sum())

# If we .count() the entries in each column, we can see how many months of entries exist per programming language.
# print(df.groupby("TAG").count())

# print(df["DATE"].loc[1])
# same like before, but the above is better to use
# print(df.DATE.loc[1])
# print(df.DATE[1])

# print(type(df["DATE"].loc[1]))

# This is not very handy. Not only will the string format always show the unnecessary 00:00:00, but we also don't get
# the benefit of working with Datetime objects, which know how to handle dates and times. Pandas can help us convert
# the string to a timestamp using the to_datetime() method.
# print(pd.to_datetime(df["DATE"].loc[1]))
# print(type(pd.to_datetime(df["DATE"].loc[1])))

df["DATE"] = pd.to_datetime(df["DATE"])
print(df.head())
