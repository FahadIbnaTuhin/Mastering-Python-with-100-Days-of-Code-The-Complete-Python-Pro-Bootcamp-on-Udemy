import pandas as pd

pd.options.float_format = '{:,.2f}'.format

df_apps = pd.read_csv('apps.csv')
df_apps.shape
df_apps.head()

# The .sample(n) method will give us n random rows.

# The axis=1 argument is necessary to indicate that you want to drop a column. If you were dropping a row, you would use
# axis=0. The default value for axis is 0, but it's good practice to explicitly specify the axis to avoid potential
# confusion.
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1)

# Challenge: How may rows have a NaN value (not-a-number) in the Ratings column? Create DataFrame called df_apps_clean
# that does not include these rows.
# The inplace=True parameter in pandas modifies the DataFrame in place, meaning it makes changes directly to the
# original DataFrame without the need to create a new one.
nan_rows = df_apps[df_apps["Rating"].isna()]
nan_rows.shape

df_apps_clean = df_apps.dropna()
df_apps_clean.shape
# FIT TIPS: I will not recommand you to use inplace=True, if you want to do, keep backup must.

# Find and Remove Duplicates
# Challenge: Are there any duplicates in data? Check for duplicates using the .duplicated() function. How many entries
# can you find for the "Instagram" app?
# Finding and Removing Duplicates
# There are indeed duplicates in the data. We can show them using the .duplicated() method, which brings up 476 rows:
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
duplicated_rows.shape

# Use .drop_duplicates() to remove any duplicates from df_apps_clean.It will only if all the columns values are
# different
df_apps_clean = df_apps_clean.drop_duplicates()
df_apps_clean.shape

# But if you search App by instagram you can see, For different reviews, duplicated are remain present
df_apps_clean[df_apps_clean["App"] == "Instagram"]

# This below means: it will delete only if the app, type and price are same
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
# Now check if it's okay
df_apps_clean[df_apps_clean["App"] == "Instagram"]

# Find Highest Rated Apps
# Challenge: Identify which apps are the highest rated. What problem might you encounter if you rely exclusively on
# ratings alone to determine the quality of an app?
df_apps_clean.sort_values("Rating", ascending=False).head()

# Find 5 Largest Apps in terms of Size (MBs)
# Challenge: What's the size in megabytes (MB) of the largest Android apps in the Google Play Store. Based on the data,
# do you think there could be limit in place or can developers make apps as large as they please?
df_apps_clean.sort_values('Size_MBs', ascending=False).head()

# Find the 5 App with Most Reviews
# Challenge: Which apps have the highest number of reviews? Are there any paid apps among the top 50?
df_apps_clean.sort_values('Reviews', ascending=False).head(15)

# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings
# First, well count the number of occurrences of each rating with .value_counts()
rating = df_apps_clean.Content_Rating.value_counts()
rating

# https://plotly.com/python-api-reference/generated/plotly.express.pie.html
import plotly.express as px
import pandas as pd
import plotly.express as px

fig = px.pie(labels=ratings.index, values=ratings.values)
fig.show()

# If youd like to configure other aspects of the chart, that you cant see in the list of parameters, you can call a
# method called .update_traces(). In plotly lingo, traces refer to graphical marks on a figure. Think of traces as
# collections of attributes. Here we update the traces to change how the text is displayed.
import pandas as pd
import plotly.express as px

fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title='Content Rating',
             names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# fig = px.pie(labels=ratings.index,
#              values=ratings.values,
#              title='Content Rating',
#              names=ratings.index
#              hole=0.6)

# Numeric Type Conversion: Examine the Number of Installs
# Check the datatype of the Installs column.
df_apps_clean.Installs.describe()
df_apps_clean.info()

# If we take two of the columns, say Installs and the App name, we can count the number of entries per level of
# installations with .groupby() and .count(). However, because we are dealing with a non-numeric data type, the ordering
# is not helpful. The reason Python is not recognising our installs as numbers is because of the comma (,) characters.
df_apps_clean[["App", "Installs"]].groupby("Installs").count()

# We can remove the comma (,) character - or any character for that matter - from a DataFrame using the strings
# .replace() method. Here were saying: replace the , with an empty string. This completely removes all the commas in the
# Installs column. We can then convert our data to a number using .to_numeric().
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(",", "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
# .astype(str): This converts the selected column to a string data type.

#  Finding the most Expensive Apps and Filtering out the Junk
df_apps_clean.Price = df_apps_clean["Price"].astype(str).str.replace("$", "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean.sort_values('Price', ascending=False).head(20)

# The most expensive apps sub $250
df_apps_clean = df_apps_clean[df_apps_clean["Price"] < 250]
df_apps_clean.sort_values("Price", ascending=False).head()

# We can work out the highest grossing paid apps now. All we need to do is multiply the values in the price and the
# installs column to get the number:
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]


# We can find the number of different categories like so:
# df_apps_clean.Category.nunique()
# Which shows us that we there are 33 unique categories.

# To calculate the number of apps per category we can use our old friend .value_counts()
# top10_category = df_apps_clean.Category.value_counts()[:10]

# But what if we look at it from a different perspective? What matters is not just the total number of apps in the
# category but how often apps are downloaded in that category. This will give us an idea of how popular a category is.
# First, we have to group all our apps by category and sum the number of installations:
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
# Then we can create a horizontal bar chart, simply by adding the orientation parameter:

h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h')

h_bar.show()
# We can also add a custom title and axis labels like so:

h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h',
               title='Category Popularity')

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

# Category Concentration - Downloads vs. Competition
# First, create a DataFrame that has the number of apps in one column and the number of installs in another:
# Then use the plotly express examples from the documentation alongside the .scatter() API referenceto create scatter plot that looks like this.
# Hint: Use the size, hover_name and color parameters in .scatter(). To scale the yaxis, call .update_layout() and specify that the yaxis should be on a log-scale like so: yaxis=dict(type='log')
# how="inner" don't take those values which has Nan value. how="outer" filled takes all and if there is nothing then
# fill with nan value
# First, we need to work out the number of apps in each category (similar to what we did previously).

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
# Then we can use .merge() and combine the two DataFrames.

cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)
# Now we can create the chart. Note that we can pass in an entire DataFrame and specify which columns should be used
# for the x and y by column name.

scatter = px.scatter(cat_merged_df, # data
                    x='App', # column name
                    y='Installs',
                    title='Category Concentration',
                    size='App',
                    hover_name=cat_merged_df.index,
                    color='Installs')

scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))

scatter.show()
