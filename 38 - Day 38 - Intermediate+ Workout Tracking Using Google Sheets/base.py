# Here we will use google sheety api, because the course api site is not working nowadays.

# https://www.youtube.com/watch?v=hyUw-koO2DA
# https://www.youtube.com/watch?v=bu5wXjz2KvU
# gspread, oauth2client, PyopenSSL

# First you need to create a project inside Google Consote Website and then enable below things from the library
# 1. Google Drive Api
# 2. Google Sheets Api

# Then, you have to get the client_email value, copy it, go to google sheet and press share and add that email there.

# QAuth 2.0 - For example, if you are building an application where users need to connect their Google Sheets to your
# service. Service Accounts -  Ideal for server-to-server interactions where the application needs to access Google
# Sheets on its own behalf without user involvement. This is common in backend services or scripts that perform tasks
# without user interaction.

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('secret_key.json', scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open('read_and_write_using_python')
sheet = workbook.sheet1

# print(f'Row Count: {sheet.row_count}\nColumn Count: {sheet.column_count}')

# To get each row as a class object
# print(sheet.range('A2:A2'))
# To get each row as a list
# print(sheet.get('A2:A5'))

# print(sheet.acell('A4').value)
# print(sheet.cell(2, 4).value)

# print(sheet.row_values(2))
# print(sheet.col_values(3))

# If your data is simple and doesn't have headers, or if you prefer working with lists, get_all_values() might be more straightforward.
# If your data has headers and you want to access values by column name, get_all_records() provides a more convenient format.
# print(sheet.get_all_records())
# print(sheet.get_all_values())
# print(sheet.get_all_cells())

# print(f'Number of rows that I have in my sheets: {len(sheet.get_all_values())}')

# Update data
# sheet.update_acell('D2', '25')
# sheet.update_cell(4, 2, 30)

# sheet.update('D2:E3', [[10, 15], [15, 20]])

#  Here, the value is '=UPPER(E2)'. This formula is telling Google Sheets to take the value in cell E2, convert it to
#  uppercase using the UPPER function, and then set the result in the specified cell (F2).
# raw=False so that It don't place the text in the cell.
# sheet.update('F2', '=UPPER(E2)', raw=False)

# sheet.update([['07/05/2024', '10:00:50', 'Cycling', 34, 250]], 'A3:E3')

# Append a row with datetime and timestamp
new_date = str(datetime.now().strftime('%d/%m/%Y'))
new_time = str(datetime.now().strftime('%H:%M:%S'))
# print(new_date, new_time)

# value_input_option="USER_ENTERED": if you manually change as a user, it will simply like user add this new row. Must
sheet.append_row([new_date, new_time, 'Running', 19, 432], value_input_option="USER_ENTERED")

# To add multiple rows:
sheet.append_rows([[new_date, new_time, 'Running', 19, 432], [new_date, new_time, 'Cycling', 34, 250],
                   [new_date, new_time, 'Swimming', 22, 385]], value_input_option="USER_ENTERED")

# For deleting single item
# sheet.delete_rows(8)
# For deleting multiple item
# sheet.delete_rows(9, 10)

