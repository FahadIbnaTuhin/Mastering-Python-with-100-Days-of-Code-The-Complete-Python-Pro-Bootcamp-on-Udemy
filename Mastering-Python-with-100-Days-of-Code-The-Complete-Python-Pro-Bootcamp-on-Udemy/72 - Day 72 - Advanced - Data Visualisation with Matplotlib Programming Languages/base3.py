import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("002 QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df["DATE"] = pd.to_datetime(df["DATE"])

reshaped_df = df.pivot(columns="TAG", index="DATE", values="POSTS")
# print(reshaped_df)

# If you use google drive -> Google Colab, then you can see the graph
# a = plt.plot(reshaped_df.index, reshaped_df["c++"])
# you can use this below also but first one is recommanded
# a = plt.plot(reshaped_df.index, reshaped_df.java)
# print(a)

# .figure() - allows us to resize our chart
# .xticks() - configures our x-axis
# .yticks() - configures our y-axis
# .xlabel() - add text to the x-axis
# .ylabel() - add text to the y-axis
# .ylim() - allows us to set a lower and upper bound

# To make our chart larger we can provide a width (16) and a height (10) as the figsize of the figure.
# plt.figure(figsize=(16, 10))
# print(plt.plot(reshaped_df.index, reshaped_df.java))

# plt.figure(figsize=(16, 10))
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.xlabel("Date", fontsize=14)
# plt.ylabel("Number of Posts", fontsize=14)
# plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df["java"])
# To compare two language, use the above and below line at the same time.
# plt.plot(reshaped_df.index, reshaped_df["python"])

# To plot all the programming languages on the same chart
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column])

# But wait, which language is which? It's really hard to make out without a legend that tells us which colour
# corresponds to each language. Let's modify the plotting code to add a label for each line based on the column name
# (and make the lines thicker at the same time using linewidth). Then let's add a legend to our chart:
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=5, label=reshaped_df[column].name)
# plt.legend(fontsize=15)


# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)
