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
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="green")
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color="blue")
#
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of sets", color="green")
# ax2.set_ylabel("Number of themes", color="blue")

# Challenge: Use the .groupby() and .agg() function together to figure out the average number of parts per set. How many
# parts did the average LEGO set released in 1954 compared to say, 2017?
parts_per_set = sets.groupby("year").agg({"num_parts": pd.Series.mean})
parts_per_set.head()
parts_per_set.tail()

# Challenge: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average
# number of parts over time using a Matplotlib scatter plot. See if you can use the scatter plot documentation before I
# show you the solution. Do you spot a trend in the chart?
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])

# LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the
# largest number of individual sets?
set_theme_count = sets["theme_id"].value_counts()
# set_theme_count[:5]
# sets["name"].loc[158]



