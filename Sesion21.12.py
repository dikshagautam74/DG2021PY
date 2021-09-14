import requests
import json
import datetime

url = "https://api.covid19india.org/v4/min/timeseries.min.json"

respond = requests.get(url, {})
# print(dir(respond))




covid_cases = json.loads(respond.text)





# Create a File by iterating in this dictionary
# we need to create a file for data of the year 2021
# File is a CSV File
# srnum,date,confirmed,tested
# 1,2021-01-01,1535699,16255271