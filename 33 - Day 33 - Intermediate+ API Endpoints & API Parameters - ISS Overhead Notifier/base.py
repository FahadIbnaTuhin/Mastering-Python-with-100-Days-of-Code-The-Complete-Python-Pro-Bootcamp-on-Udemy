# 1XX: Hold On (Something is happening it is not fine)
# 2XX: Here You Go
# 3XX: Go Away (You don't have permission to get that thing so go away)
# 4XX: Me the Programmer Made some error
# 5XX: I Screwed Up (Maybe the server down, or the website or anything with the website api)

import requests

# Url From this webpage: https://open-notify.org/Open-Notify-API/ISS-Location-Now/
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)

# if response.status_code != 200:
#     raise Exception("Something bad happened")

# if response.status_code == 404:
#     raise Exception("Not Found")
# elif response.status_code == 401:
#     raise Exception("You don't have the permission to get the data.")

#  For different kind of status, you can use the below, it will provide the error you got easily
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

position = (longitude, latitude)
print(position)
