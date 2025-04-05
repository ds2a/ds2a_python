import requests
import json

# Make the GET request to the horoscope API
response = requests.get("https://api.currencyfreaks.com/v2.0/rates/latest?apikey=b149d7191fde4c46bee6d6cf993d82cf")
# response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convert the response to JSON

# response.
print(data['rates']['INR'])

# Store the JSON data in a file
# with open("currency_exchange.json", "w") as file:
#     json.dump(data, file)

print("Data stored successfully!")