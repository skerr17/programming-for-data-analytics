# This program prints out the bank holidays that happen in Northern Ireland
# Auther: Stephen Kerr

import requests

url = 'https://www.gov.uk/bank-holidays.json'

response = requests.get(url)
data = response.json()

'''
# Basic print of the events in Northern Ireland

for event in data['northern-ireland']['events']:
    print(f"{event['title']} : {event['date']}")

'''

# Print only the bank holidays that are unique to Northern Ireland

events_in_england_and_wales = [event['title'] for event in data['england-and-wales']['events']]
events_in_scotland = [event['title'] for event in data['scotland']['events']]

for event in data['northern-ireland']['events']:
    if event['title'] in events_in_england_and_wales or event['title'] in events_in_scotland:
        pass
    else:        
        print(f"{event['title']} : {event['date']}")

