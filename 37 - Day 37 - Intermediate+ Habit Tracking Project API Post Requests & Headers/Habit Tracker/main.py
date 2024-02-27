from datetime import datetime
import requests

USERNAME = "kilaw"
TOKEN = "a68s7dfads0f7asdf"
GRAPH_ID = "graph1"

user_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Number of Eating time",
    "unit": "bar",
    "type": "int",
    "color": "ajisai"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)
# Your created graph link : step 3: Get the graph!
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API.
# https://pixe.la/v1/users/kilaw/graphs/graph1.html

# To post for today dynamically
# for the date key: It is specified in yyyyMMdd format. [Read the documentation]
post_endpoint1 = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
post_params1 = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many times did you eat yesterday? ")
}
response = requests.post(url=post_endpoint1, json=post_params1, headers=header)
print(response.text)

# To post for any specific date manually
post_endpoint2 = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2024, month=1, day=25)
post_params2 = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many times did you eat yesterday? ")
}
# response = requests.post(url=post_endpoint2, json=post_params2, headers=header)
# print(response.text)

update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "1"
}
# put() to update the data you want
# response = requests.put(url=update_endpoint, json=update_params, headers=header)
# print(response.text)

delete_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete() for deleting the data you want
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
