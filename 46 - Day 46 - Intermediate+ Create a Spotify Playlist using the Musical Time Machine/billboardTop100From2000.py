from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.billboard.com/charts/hot-100/2000-01-01/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

# titles = [title.getText().strip() for title in soup.find_all("h3", id="title-of-a-story",
#                                                             class_="u-line-height-normal@mobile-max")]

# After "c-title", there were two spaces. After removing one, it is working
titles = [title.getText().strip() for title in soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-"
    "bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal"
    "@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
print(titles)
artists = [artist.getText().strip() for artist in soup.find_all("span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
print(artists)
