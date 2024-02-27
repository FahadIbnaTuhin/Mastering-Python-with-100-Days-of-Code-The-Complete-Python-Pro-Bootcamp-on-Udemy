from datetime import datetime
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def write_on_google_sheets(user_data):
    scopes = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scopes=scopes)
    file = gspread.authorize(creds)
    workbook = file.open('workoutTrainingUsingGoogleSheets')
    sheet = workbook.sheet1

    sheet.append_row([user_data['date'], user_data['time'], user_data['food'], user_data['calories']],
                     value_input_option='USER_ENTERED')


def response_from_api(food):
    API_KEY = '.'
    url = 'https://api.spoonacular.com/recipes/guessNutrition'

    params = {
        'apiKey': API_KEY,
        'title': food
    }

    headers = {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()['calories']['value']
    return data


date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')

food_name = input("What food have you eaten today? ")

user_input = {
    'date': date,
    'time': time,
    'food': food_name,
    'calories': response_from_api(food_name)
}

write_on_google_sheets(user_input)
