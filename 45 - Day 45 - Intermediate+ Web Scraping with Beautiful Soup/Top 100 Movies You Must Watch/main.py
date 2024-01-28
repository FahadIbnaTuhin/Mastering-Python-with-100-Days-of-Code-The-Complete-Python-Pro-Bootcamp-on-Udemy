from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.find_all("h3", class_="listicleItem_listicle-item__title__BfenH")
# print(articles)

# movie_titles = [title.getText() for title in articles]
# # Reverse style
# movies = movie_titles[::-1]
#
# with open("movies.txt", "w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")

with open("movies.txt", "w") as file:
    for i in range(len(articles) - 1, -1, -1):
        file.write(f"{articles[i].getText()}\n")
