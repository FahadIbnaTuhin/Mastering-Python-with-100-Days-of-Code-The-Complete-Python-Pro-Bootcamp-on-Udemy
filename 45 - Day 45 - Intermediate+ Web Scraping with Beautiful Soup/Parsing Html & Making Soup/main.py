# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# If "html.parser" not working, then you can use "lxml"
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.getText())

# print(soup)
# print(soup.prettify())

# To get first anything
# print(soup.a)
# print(soup.li)

all_anchor_tag = soup.find_all("a")
# print(all_anchor_tag)
# for tag in all_anchor_tag:
    # print(tag.getText())
    # print(tag.get("href"))

# find_all() give you everything but find() will give you only the first one
# heading = soup.find(name="h1", id="name")
# print(heading)

# python has class keyword, so here use class_
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.get("class"))

# select_one gives us the first matching item while select gives all matching items
# "p a" --> think like css. Inside p tag then a tag
company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one("#name")
# print(name)

headings = soup.select(".heading")
# print(headings)
