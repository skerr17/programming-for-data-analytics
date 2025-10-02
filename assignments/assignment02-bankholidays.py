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

# first get each list of event titles in England and Wales and Scotland
events_in_england_and_wales = [event['title'] for event in data['england-and-wales']['events']]
events_in_scotland = [event['title'] for event in data['scotland']['events']]

unqiue_northern_ireland_events = {}

# loop through the events in Northern Ireland and print only those not in the other two lists
for event in data['northern-ireland']['events']:
    if event['title'] not in events_in_england_and_wales and event['title'] not in events_in_scotland:
        # checking if the event is already in the unique events dict if not create a new list
        if event['title'] not in unqiue_northern_ireland_events:
            unqiue_northern_ireland_events[event['title']] =[]
        # append the date to the list of dates for that event title
        unqiue_northern_ireland_events[event['title']].append(event['date'])

print("Unique Northern Ireland Bank Holidays")
print('-----------------------------------')

# print the unique events
for title, dates in unqiue_northern_ireland_events.items():
    print(f"{title} : {', '.join(dates)}")



