import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import weatherInput
import emailSend 

scope = ["https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open('weatherbotdata').sheet1

# Seperation of data into variables
firstName = sheet.col_values(2)
lastName = sheet.col_values(3)
phoneNumber = sheet.col_values(4)
city = sheet.col_values(5)
carrier = sheet.col_values(6)
state = sheet.col_values(7)

# Creating Dictionary to Store Data
uInfo = {}

# Putting User info in a Dictionary
for i in range(1, len(firstName)):
    uInfo[firstName[i]] = [phoneNumber[i], city[i], state[i], carrier[i]]
    

# Excecuting Functions
for key, value in uInfo.items():    
    weatherInfo = weatherInput.weatherData(value)
    if weatherInfo == [-1,-1]:
        print('ERROR')
        break
    message = emailSend.bodyFormation(key, value[1], weatherInfo[0], weatherInfo[1])
    email = emailSend.emailFormation(value[0], value[3])
    emailSend.emailSending(message,email)
    
