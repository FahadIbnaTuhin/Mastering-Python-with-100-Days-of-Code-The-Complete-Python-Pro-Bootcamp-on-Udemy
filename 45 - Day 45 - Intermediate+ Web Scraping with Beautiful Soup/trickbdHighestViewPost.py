from bs4 import BeautifulSoup
import requests

response = requests.get("https://trickbd.com/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
# print(soup)

articles = soup.find_all("h3", class_="p_title")[5:]
article_titles = []
article_links = []
for article in articles:
    title = article.find("a").getText()
    article_titles.append(title.replace("\n", ""))
    link = article.find("a").get("href")
    article_links.append(link)

print(article_titles)
print(article_links)

views = [int(view.getText().replace(",", "")) for view in soup.find_all("span", class_="post-views-count")[5:]]
print(views)

pos = views.index(max(views))
print(f"Title: {article_titles[pos]}\nLink: {article_links[pos]}")
