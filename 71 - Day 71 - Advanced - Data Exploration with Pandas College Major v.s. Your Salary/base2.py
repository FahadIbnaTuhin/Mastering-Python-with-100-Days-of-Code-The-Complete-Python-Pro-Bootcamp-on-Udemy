# A low-risk major is a degree where there is a small difference between the lowest and highest salaries.
# In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small,
# then you can be more certain about your salary after you graduate.
import pandas as pd

df = pd.read_csv("003 salaries-by-college-major.csv")

final_df = df.dropna()
# print(final_df)

spread_col = final_df["Mid-Career 90th Percentile Salary"] - final_df["Mid-Career 10th Percentile Salary"]
final_df.insert(1, "spread", spread_col)
# print(final_df.head())

low_risk = final_df.sort_values("spread")
print(low_risk[["Undergraduate Major", "spread"]].head())

# High Pay Spread:
# A high difference suggests that individuals in that major experience substantial pay increases as they progress in their careers.
# It may indicate that the skills and expertise gained over time in that field are highly valued in the job market.
# The major might lead to lucrative career opportunities or positions with high earning potential.
# Low Pay Spread:
# A low difference implies that the increase in pay from early to mid-career is relatively modest.
# It may suggest that the major provides steady, but not necessarily significantly higher, income growth as professionals gain experience.
# The major may not be associated with as rapid career advancement or high earning potential compared to majors with a higher pay spread.

top5_high_90th = final_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
print(top5_high_90th[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

highest_spread = final_df.sort_values(by="spread", ascending=False)
print(highest_spread[["Undergraduate Major", "spread"]].head())

highest_spread = final_df.sort_values("Mid-Career Median Salary", ascending=False)
print(highest_spread[["Undergraduate Major", "Mid-Career Median Salary"]].head())



