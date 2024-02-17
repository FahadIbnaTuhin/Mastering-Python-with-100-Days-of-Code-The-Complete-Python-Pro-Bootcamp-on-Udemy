# Here I will work with recent 2023 Highest Paying Jobs Data
# https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors
import pandas as pd

df = pd.read_csv("highestPayingJobs2023.csv")

# df.replace('-', pd.NaT): This replaces all occurrences of "-" with NaN (Not a Number) in the entire
# DataFrame. pd.NaT is a special value representing missing or undefined data.
df = df.replace("-", pd.NaT)
df = df.dropna()
# print(df.isna())

# Identifying the top-paying majors based on early pay - Physician Assistant Studies - 109600.0
# print(df[["Major", "Early Career Pay"]].loc[df["Early Career Pay"].idxmax()])

# Identifying the lowest-paying majors based on early pay - Global & International Studies - 59400.0
# print(df[["Major", "Early Career Pay"]].loc[df["Early Career Pay"].idxmin()])

# Identifying the top-paying majors based on mid-career pay: Petroleum Engineering - 212,500.00
# print(df[["Major", "Mid-Career Pay"]].loc[df["Mid-Career Pay"].idxmax()])

# Identifying the lowest-paying majors based on mid-career pay - Information & Decision Sciences - 126,800.00
# print(df[["Major", "Mid-Career Pay"]].loc[df["Mid-Career Pay"].idxmin()])

# Comparing the pay difference between early and mid-career for specific majors.
spread_column = df["Mid-Career Pay"] - df["Early Career Pay"]
df.insert(1, "spread", spread_column)

# High Pay Spread:
# A high difference suggests that individuals in that major experience substantial pay increases as they progress in
# their careers.
# Low Pay Spread:
# A low difference implies that the increase in pay from early to mid-career is relatively modest.

# low_pay_spread = df.sort_values("spread")
# print(low_pay_spread[["Major", "spread"]].head())
# 56  Physician Assistant Studies  26900.0
# 60    Metallurgical Engineering  44700.0
# 62           Mining Engineering  47800.0
# 98         Plastics Engineering  48000.0
# 96            Packaging Science  49000.0

# high_pay_spread = df.sort_values("spread", ascending=False)
# print(high_pay_spread[["Major", "spread"]].head())
# 0                         Petroleum Engineering  115000.0
# 2                            Interaction Design   98900.0
# 4                              Building Science   94100.0
# 1  Operations Research & Industrial Engineering   93500.0
# 5                         Actuarial Mathematics   89300.0

# Highest Mid career pay
# highest_mid_pay = df.sort_values("Mid-Career Pay", ascending=False)
# print(highest_mid_pay[["Major", "Mid-Career Pay"]].head())
# 0                         Petroleum Engineering        212500.0
# 1  Operations Research & Industrial Engineering        191800.0
# 2                            Interaction Design        173600.0
# 3              Applied Economics and Management        164400.0
# 4                              Building Science        163100.0

# high level of meaning or job satisfaction
# high_job_satisfaction = df.sort_values("% High Meaning", ascending=False)
# print(high_job_satisfaction[["Major", "% High Meaning"]].head())
# 56    Physician Assistant Studies            83%
# 12                       Pharmacy            79%
# 8   Optical Science & Engineering            73%
# 24   Electrical Power Engineering            72%
# 69   Biomedical Engineering (BME)            71%
