# A low-risk major is a degree where there is a small difference between the lowest and highest salaries.
# In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small,
# then you can be more certain about your salary after you graduate.
import pandas as pd

df = pd.read_csv("003 salaries-by-college-major.csv")

final_df = df.dropna()
# print(final_df)

spread_col = final_df["Mid-Career 90th Percentile Salary"] - final_df["Mid-Career 10th Percentile Salary"]
final_df.insert(1, "spread", spread_col)
print(final_df.head())

low_risk = final_df.sort_values("spread")
print(low_risk.head())

top5_high_90th = final_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
print(top5_high_90th.head())

largest_difference_between_high_and_low_earners = final_df.sort_values(by="spread", ascending=False)
print(largest_difference_between_high_and_low_earners.head())


