# Assignment: Bank Holidays in Northern Ireland
# This program prints out the bank holidays that happen in Northern Ireland
# Author: Stephen Kerr

import requests

url = 'https://www.gov.uk/bank-holidays.json'



# reference: error handling for the request module can be seen here: https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/
# also see here: https://www.geeksforgeeks.org/python/response-json-python-requests/


try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
    exit()
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
    exit()



try:
    data = response.json()
except ValueError: 
    print("Error: Invalid JSON return from API.")
    exit()





'''
# Basic print of the events in Northern Ireland

for event in data['northern-ireland']['events']:
    print(f"{event['title']} : {event['date']}")

'''

# Print only the bank holidays that are unique to Northern Ireland

# first get each list of event titles in England and Wales and Scotland
events_in_england_and_wales = [event['title'] for event in data['england-and-wales']['events']]
events_in_scotland = [event['title'] for event in data['scotland']['events']]

unique_northern_ireland_events = {}

# loop through the events in Northern Ireland and print only those not in the other two lists
for event in data['northern-ireland']['events']:
    if event['title'] not in events_in_england_and_wales and event['title'] not in events_in_scotland:
        # checking if the event is already in the unique events dict if not create a new list
        if event['title'] not in unique_northern_ireland_events:
            unique_northern_ireland_events[event['title']] =[]
        # append the date to the list of dates for that event title
        unique_northern_ireland_events[event['title']].append(event['date'])

print("Unique Northern Ireland Bank Holidays")
print('-----------------------------------')

# print the unique events
for title, dates in unique_northern_ireland_events.items():
    print(f"{title} : {', '.join(dates)}")