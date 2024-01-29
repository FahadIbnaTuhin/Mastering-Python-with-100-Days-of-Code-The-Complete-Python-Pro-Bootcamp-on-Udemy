# https://www.youtube.com/watch?v=WAmEZBEeNmg
import base64
import json
import os
import requests
from dotenv import load_dotenv

# This will automatically load our environment variable for us.
# For this create .env file and .env and this main will be in the same directory
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
# print(client_id, client_secret)


def get_token():
    # Here we are working with client-credentials-flow api, which is a api which is perfect for our backend development
    # https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


# This is what we need to use in any future headers when we are trying to send a request to the API to get some artist
# information playlist. It will kind of construct the header that we need whenever we're sending another request
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    # limit=1 means getting the first artist when searched by this
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    # print(json_result)

    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


token = get_token()
# print(token)

result = search_for_artist(token, "ACDC")
# print(result)
# print(result["name"])

artist_id = result["id"]
# print(artist_id)

songs = get_songs_by_artist(token, artist_id)
# print(songs)
for index, song in enumerate(songs):
    print(f"{index + 1}. {song['name']}")
