import pandas as pd
import matplotlib.pyplot as plt

sets = pd.read_csv("data/sets.csv")
# However, sometimes you want to run even more operations based on a particular DataFrame column. This is where the
# .agg() method comes in.Note, the .agg() method takes a dictionary as an argument. In this dictionary, we specify which
# operation we'd like to apply to each column. In our case, we just want to calculate the number of unique entries in
# the theme_id column by using our old friend, the .nunique() method.
themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
print(themes_by_year.head())
print(themes_by_year.tail())

# Challenge: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e.,
# exclude 2020 and 2021).
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# Line Charts with Two Seperate Axes









