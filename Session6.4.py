"""
Search Sort and Filter
"""

drivers = [
    {
        "name": "John",
        "status": 0,
        "distance": 5
    },
    {
        "name": "Joe",
        "status": 0,
        "distance": 15
    },
    {
        "name": "Jack",
        "status": 1,
        "distance": 3
    },
    {
        "name": "Lee",
        "status": 1,
        "distance": 8
    },
    {
        "name": "Fionna",
        "status": 0,
        "distance": 14
    }

]

print("DRIVERS")
for driver in drivers:
    print("*"*10)
    print("{name}\n{status} | {distance}".format_map(driver))
    print("*"*10)
    print()

# SEARCHING THE DRIVER ACCORDING TO OUR CONDITION
print("SEARCH THE DRIVER")
status = int(input("Enter Offline(0) Online(1) status :"))
distance = int(input("Enter distance"))

# found = False

for driver in drivers:
   if driver["status"] == status and driver["distance"] == distance:
       print("*" * 10)
       print("{name}\n{status} | {distance}".format_map(driver))
       print("*" * 10)
       #found = True
       break
   else:
       print("driver not found")
       break

#if not found:
#     print("Sorry! Driver Not Found")

# this filtering makes us available the drivers which are satisfying our condition below
# like if we are giving status input as 1 , it will print us the drivers those are online
# as giving distance input(filter2) as 15,so it will print us the drivers those are covering distance less than 15.
#from both the conditions,it will print us the drivers those are online(1) and with distance(less than 15).
print("FILTER THE DRIVERS")
filter1 = int(input("Enter filter1 for status(0/1) :"))
filter2 = int(input("Enter filter2 for distance :"))

for driver in drivers:
     if driver["status"] == filter1 and driver["distance"] <= filter2:
         print("*" * 10)
         print("{name}\n{status} | {distance}".format_map(driver))
         print("*" * 10)

#SORTING  -> bubble sort
# sort the drivers in an ascending order
print("SORTED DRIVERS")
for i in range(0, len(drivers)):
    for j in range(0, len(drivers) - i - 1):      # this loop runs first from 0-4 and after completing it will move to the outer loop and in outer loop i becomes 1 and then again innerj loop runs from 0-3 and this process continues
         if drivers[j]["distance"] > drivers[j + 1]["distance"]:
            # swapping -> drivers[j] with drivers[j+1] and drivers[j+1] with drivers[j]
           drivers[j], drivers[j + 1] = drivers[j + 1], drivers[j]

for driver in drivers:
    print("^" * 10)
    print("{name}\n{status} | {distance}".format_map(driver))
    print("^" * 10)
