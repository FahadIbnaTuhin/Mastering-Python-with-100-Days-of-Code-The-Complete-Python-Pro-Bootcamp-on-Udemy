import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
colors.head()

# We see that there are 5 columns, which include the name of the colour and its corresponding RGB value. To find the number of unique colours, all we need to do is check if every entry in the name column is unique:
# colors['name'].nunique()

# Find the number of transparent colours
# colors.groupby("is_trans").count()
colors.is_trans.value_counts()

# ### Understanding Lego Themes vs Lego Sets
# Walk into a lego store and you will see their products organized by theme. Their theme include Star Wars, Bat Man,
# Harry Potter, many more.
# <img src="https://i.imgur.com/aKcwkSx.png" alt="Not Found">
# A Lego **Set** is particular box of Lego or product. Therefore a single theme typically has many different themes.
# <img src="https://i.imgur.com/whBlog.png" width="500">

# Challenge: In which year were the first LEGO sets released and what were these sets called?
sets = pd.read_csv("data/sets.csv")
# sets.sort_values("year").head()

# Challenge: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer
# in the year the company started?
# sets[sets["year"] == 1949]

# Challenge: Find the top 5 LEGO sets with the most number of parts.
# sets.sort_values("num_parts", ascending=False).head()

# Challenge: Use .groupby() and .count() to show the number of LEGO sets released year-on-year. How do the number of
# sets released in 1955 compare to the number of sets released in 2019?
sets_by_year = sets.groupby("year").count()
# sets_by_year["set_num"].head()
# sets_by_year["set_num"].tail()

# Challenge: Show the number of LEGO releases on a line chart using Matplotlib.
# Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data from
# your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax
# will work on Pandas DataFrames.
sets_by_year = sets.groupby("year").count()
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

