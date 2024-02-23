import requests

# GENDER = 'Male'
# WEIGHT_KG = 40
# HEIGHT_CM = 167.64
# AGE = 20

# gender = input('Please input your gender: ')
# weight_kg = input('Please input your weight in kg: ')
# height_cm = input('Please input your height in cm: ')
# age = int(input('Please input your age: '))

API_KEY = '6df8be01919444048ffa5b8f4ddb3f42'
# url = 'https://api.spoonacular.com/recipes/716429/information?apiKey=&includeNutrition=true'

url = 'https://api.spoonacular.com/recipes/guessNutrition'

params = {
    'apiKey': API_KEY,
    'includeNutrition': 'true'
}

headers = {
    'Content-Type': 'application/json',
    'title': input('Enter the food name: ')
}

response = requests.get(url, params=params, json=headers)

print(response.text)


print()

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
#
# scopes = [
#     'https://www.googleapis.com/auth/drive',
#     'https://www.googleapis.com/auth/spreadsheets'
# ]
#
# creds = ServiceAccountCredentials.from_json_keyfile_name('workouttrackingusingsheets.json', scopes=scopes)
# file = gspread.authorize(creds)
# workbook = file.open('workoutTrainingUsingGoogleSheets')
# sheet = workbook.sheet1
#
# print(sheet.row_count)







