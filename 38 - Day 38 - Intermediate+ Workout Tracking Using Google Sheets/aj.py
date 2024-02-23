import requests

API_KEY = '.'

url = 'https://api.spoonacular.com/recipes/guessNutrition'

# Parameters in the URL
params = {
    'apiKey': API_KEY,
    'title': input('Enter any food name: ')
}

# Headers with API key and Content-Type
headers = {
    'x-api-key': API_KEY,  # The API key can also be included in the headers
    'Content-Type': 'application/json',
}

# Making the GET request
response = requests.get(url, params=params, headers=headers)
print(response.text)
