"""
some built in functions in python
"""

numbers = list(range(10,101,10))
print("numbers are:", numbers)
numbers.append(70)
print(numbers)

reversed_numbers = list(reversed(numbers))
print("numbers after reversing:", reversed_numbers)

print("reversed numbers after sorting:", sorted(reversed_numbers))

print("index of 50 in list is :", numbers.index(50))
print("counting of 70 in list is:", numbers.count(70))

data = [1, 43, 5, 23, 12]
print("data :", data)
data.sort()
print("sorted data:", data)

data.reverse()
print("data after reversing:", data)

data.remove(43)
print("data after removing 43 :", data)

data.pop(2)
print("popping 2nd index number :", data)

data.append(20)
print("data after appending 20 :", data)

data.insert(2,10)
print("inserting 10 at 2nd index:", data)

# remove all elemnets from the list
data.clear()
print(data)
print("elements in list/length of list :", len(data))



