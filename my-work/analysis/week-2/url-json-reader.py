# In this program we will read data in json format 
# from a url to the consol Lab 1 Q 6, 7 (data type is Dict), 8
# Auther: Stephen Kerr


import requests


url = 'https://www.gov.uk/bank-holidays.json'


response = requests.get(url)

data = response.json()

#print(data)

#print(type(data))

print(data.keys())

print(data['northern-ireland'].keys())

# first event in northern Ireland
print(data['northern-ireland']['events'][0])