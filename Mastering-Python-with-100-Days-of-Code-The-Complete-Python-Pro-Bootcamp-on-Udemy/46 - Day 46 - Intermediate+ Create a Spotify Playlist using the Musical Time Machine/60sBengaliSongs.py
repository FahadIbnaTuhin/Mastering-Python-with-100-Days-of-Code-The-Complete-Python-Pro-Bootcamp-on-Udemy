from bs4 import BeautifulSoup
import requests

response = requests.get("https://wynk.in/music/playlist/evergreen-60s-bengali/bb_1520872412485")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")


# song_titles = [title.get("title") for title in soup.find_all("a", class_="jsx-7c093e1a359b5feb text-title font-normal line-clamp-1 md:line-clamp-2 text-sm hover:underline")]
# song_artists = [artist.getText() for artist in soup.find_all("span", class_="text-items hover:underline underline")]

# print(len(song_titles))
# print(len(song_artists))

songs = soup.find_all("div", class_="jsx-7c093e1a359b5feb flex w-full pr-8 md:pr-10")
song_titles = []
song_artists = []
for song in songs:
    title = song.select_one("div div a").get("title")
    # last class is ".text-items hover:underline underline" but gap is not allowed so used only ".text-items"
    artist = song.select_one("div div span a .text-items")
    song_titles.append(title)
    song_artists.append(artist)

# print(songs)
# print(song_titles)
# print(song_artist)

with open("60sBengaliSongs.txt", "w") as file:
    for i in range(len(songs)):
        file.write(f"{i + 1}. Title: {song_artists[i]} & Artist: {song_artists[i]}\n")
