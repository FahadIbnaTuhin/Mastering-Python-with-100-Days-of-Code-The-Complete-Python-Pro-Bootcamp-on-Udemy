import pandas as pd

# This give the number of unique things
df_apps_clean.Genres.nunique()
# This give the things which are unique
df_apps_clean.Genres.unique()

len(df_apps_clean.Genres.unique())
df_apps_clean.Genres.value_counts(ascending=True)[:5]

# We somehow need to separate the genre names to get a clear picture. This is where the strings .split() method comes in
# handy. After weve separated our genre names based on the semi-colon, we can add them all into a single column with
# .stack() and then use .value_counts().
# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
# The expand=True parameter is used to expand the split lists into separate columns, creating a DataFrame with one
# column for each genre.

bar = px.bar(x=num_genres.index[:15],
             y=num_genres.values[:15],
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')
bar.update_layout(xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
bar.show()

# We see that the majority of apps are free on the Google Play Store. But perhaps some categories have more paid apps
# than others. Lets investigate. We can group our data first by Category and then by Type. Then we can add up the number
# of apps per each type. Using as_index=False we push all the data into columns rather than end up with our Categories
# as the index.
# df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
# df_free_vs_paid.head()

# Solution: Create Box Plots for the Number of Installs
# From the hover text in the chart, we see that the median number of downloads for free apps is 500,000, while the median number of downloads for paid apps is around 5,000! This is massively lower.
# box = px.box(df_apps_clean,
#              y='Installs',
#              x='Type',
#              color='Type',
#              notched=True,
#              points='all',
#              title='How Many Downloads are Paid Apps Giving Up?')
#
# box.update_layout(yaxis=dict(type='log'))
# box.show()
# But does this mean we should give up on selling a paid app? Lets see how much revenue we would estimate per category.



























