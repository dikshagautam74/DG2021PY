# DICTIONARY

my_data = {}
print("my data:", my_data, type(my_data), len(my_data))

my_data = {101:"jack", 210:"robin", 301:"joe"}
print("my data:", my_data, type(my_data), len(my_data))
print(max(my_data))
print(min(my_data))


print(my_data[210])
# trying to print the key value which is not in the dictionary
#print(my_data[400])  -> KeyError

# printing key value with get() function
print(my_data.get(210))

# printing key value which is not in dict. with get() function will not give ERROR
# it will print u NONE as a default value
print(my_data.get(400))

# deleting key 300
# del my_data[301]
# print(my_data)

"""
removing 101 key
my_data.pop(101)
print(my_data)
"""

# it will remove last key
pair = my_data.popitem()
print(pair)
print(my_data)

print()

covid_cases = {}.fromkeys(["active","confirmed", "recovered"], 0)
print(covid_cases)

covid_cases["active"] = 30456
covid_cases["confirmed"] = 40467
covid_cases["recovered"] = 50489

# it will print you items of dictionary both with key and value
items = covid_cases.items()
print(items,type(items))

# it will also print you items of dictionary both with key and value but in a new line
for item in covid_cases.items():
    print(item[0],item[1])

# it will print you keys of dictionary
keys = covid_cases.keys()
print("keys:", keys)

# it will also print you keys of dictionary
for key in keys:
  print(key)

# enumerate iterates the covid cases
for idx,data in enumerate(covid_cases):
    print(idx,data)


"""
this is same as above but it doesn't use enumerate()

for key in keys:
    print(idx, key, covid_cases[key])
    idx+=1
"""



