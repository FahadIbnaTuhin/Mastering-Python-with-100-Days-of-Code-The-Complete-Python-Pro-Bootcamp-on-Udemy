# A schema is just how the database is organised

# themes = pd.read_csv("data/themes.csv")
# themes[themes["name"] == "Star Wars"]

# The themes.csv file has the actual theme names. The sets .csv has theme_ids which link to the id column in the
# themes.csv.
# Challenge: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many ids correspond to
# this name in the themes.csv? Now use these ids and find the corresponding the sets in the sets.csv (Hint: you('ll need to'
# ' look for matches in the theme_id column))
# themes = pd.read_csv("data/themes.csv")
# themes[themes["name"] == "Star Wars"]
# sets[sets.theme_id == 18]
# sets[sets.theme_id == 209]

# set_theme_count = sets["theme_id"].value_counts()
# set_theme_count[:5]

# set_theme_count = sets["theme_id"].value_counts()
# set_theme_count = pd.DataFrame({"id": set_theme_count.index, "set_count": set_theme_count.values})
# set_theme_count.head()

# To .merge() two DataFrame along a particular column, we need to provide our two DataFrames and then the column name on
# which to merge. This is why we set on='id'. Both our set_theme_count and our themes DataFrames have a column with this
# name.
# themes = pd.read_csv("data/themes.csv")
# merged_df = pd.merge(set_theme_count, themes, on='id')
# merged_df[:3]

# plt.bar(merged_df.name[:10], merged_df.set_count[:10])

# plt.figure(figsize=(14,8))
# plt.xticks(fontsize=14, rotation=45)
# plt.yticks(fontsize=14)
# plt.ylabel('Nr of Sets', fontsize=14)
# plt.xlabel('Theme Name', fontsize=14)
#
# plt.bar(merged_df.name[:10], merged_df.set_count[:10])

