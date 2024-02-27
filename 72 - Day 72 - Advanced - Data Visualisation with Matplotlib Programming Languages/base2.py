import pandas as pd

# --------------------------------------Understand Properly-------------------------------------------
# test_df = pd.DataFrame({
#     "Age": ["Young", "Young", "Young", "Young", "Old", "Old", "Old", "Old"],
#     "Actor": ["Jack", "Arnold", "Keanu", "Sylvester", "Jack", "arnold", "Keanu", "Sylvester"],
#     "Power": [100, 80, 25, 50, 99, 75, 5, 30]
# })
#
# # print(test_df)
# pivoted_df = test_df.pivot(columns="Actor", index="Age", values="Power")
# print(pivoted_df.head())
# However, there's one very important thing to notice. What happens if a value is missing? In the example above there's
# no value for old Sylvester. In this case, the .pivot() method will insert a NaN value.
# --------------------------------------Understand End-------------------------------------------


df = pd.read_csv("002 QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df["DATE"] = pd.to_datetime(df["DATE"])
# print(df)

reshaped_df = df.pivot(columns="TAG", index="DATE", values="POSTS")
print(reshaped_df.fillna(0))
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# Stack overflow was created in 2008 and at that time, c# is most used and now at present python
# print(reshaped_df.count())
# we want to substitute the number 0. for each NaN value in the DataFrame.We can do this with the.fillna() method.
reshaped_df = reshaped_df.fillna(0)
# print(reshaped_df)
# Here we are using the .isna() method that we've used before, but we're chaining two more things: the values attribute
# and the any() method. This means we don't have to search through the entire DataFrame to spot if .isna() is True.
print(reshaped_df.isna().values.any())



