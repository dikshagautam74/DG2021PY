import json

covid_case = {
    "state": "Punjab",
    "confirmed": 344241,
    "active": 1233,
    "vaccinated": [13232, 2101]
}

print(covid_case, type(covid_case))

# we can convert dictionary to JSON
# JSON is just a string representation of Dictionary

# it converts the data type(dict) of covid cases to string
json_data = json.dumps(covid_case)
print(json_data, type(json_data))
#
# json_data = str(covid_case)
# print(json_data, type(json_data))

# it agains converts the data type from str to of what type(dict) we have made the data
dictionary_data = json.loads(json_data)
print(dictionary_data, type(dictionary_data))