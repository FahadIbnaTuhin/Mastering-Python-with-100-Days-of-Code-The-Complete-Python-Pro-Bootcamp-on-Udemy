# find and find_all is better than select or select_all as it works with more complex and concise style
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article in articles:
    text = article.find("a").getText()
    link = article.find("a").get("href")
    article_texts.append(text)
    article_links.append(link)

# article_votes = [vote.getText() for vote in soup.find_all("span", class_="score")]
article_votes = [int(vote.getText().split()[0]) for vote in soup.find_all("span", class_="score")]

print(article_texts)
print(article_links)
print(article_votes)

# to get only the number not the rest of the thing which is string
# print(int(article_votes[0].split()[0]))

# Print the title and the link with the highest number of upvotes
pos = article_votes.index(max(article_votes))
print(f"{article_texts[pos]}: {article_links[pos]}")
