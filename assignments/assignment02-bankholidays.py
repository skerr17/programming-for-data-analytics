# This program prints out the bank holidays that happen in Northern Ireland
# Auther: Stephen Kerr

import requests

url = 'https://www.gov.uk/bank-holidays.json'

response = requests.get(url)
data = response.json()

for event in data['northern-ireland']['events']:
    print(f"{event['title']} : {event['date']}")

