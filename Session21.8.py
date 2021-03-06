import requests
import json

url = "https://api.covid19india.org/v4/min/timeseries.min.json"
response = requests.get(url)
# print(response.text)
print(type(response.text))   # it will give u str data type

# loads converts the data type from str to dict
covid_cases = json.loads(response.text)
# print(covid_cases)
print(type(covid_cases))

# Create a File by iterating in this dictionary
# we need to create a file for data of the year 2021
# File is a CSV File
# srnum,date,confirmed,tested
# 1,2021-01-01,1535699,16255271