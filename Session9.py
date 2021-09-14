"""
 Sequences in  python
 list
 tuple
 set
 dictionary
 string

 Properties of indexing
 1.Indexing
 2.Negative Indexing
 3.Slicing
 4.Concatenation
 5.Multiplicity
 6.Membership Testing

"""

class user:
    pass


user1 = user()

string = "hello"
print("string is: ", string, type(string), hex(id(string)))


dict = {
    "name" : "robin",
    "age" : 10,
    "email" : "robin@example.com",
    "phone" : "+91 99999 44334"
}
print("dict is: ", dict, type(dict), hex(id(dict)))


set = {100,200,300}
print("set is: ", set, type(set), hex(id(set)))


data = [1,2,3]
print("data is: ", data, type(data), hex(id(data)))

my_data = (10,20,30)
print(" my data is: ", my_data, type(my_data), hex(id(my_data)))
print(max(my_data), min(my_data))

print()

#INDEXING
print("index :", my_data[0])
print("index :", data[0])
#print("index :", set[0])   --> ERROR
#print("index :", dict[0])   --> ERROR
print("index :", dict["name"])  # it can be done like this in dictionary
print("index :", string[0])

print()

#NEGATIVE INDEXING
# indexing starts from back and index starts from -1 not from 0
# index   -3  -2  -1
#  list  [10, 20, 30]
print(" NEGATIVE index :", my_data[-1])
print("NEGATIVE index :", data[-1])
#print("NEGATIVE index :", set[-1])   --> ERROR
#print("index :", dict[-1])   --> ERROR
print("NEGATIVE index :", string[-1])

print()

# SLICING
# starting from 10 and goes to 101 with the increment of 10
numbers = list(range(10,101,10))
# at left there should always be lesser number
# if at left side there's nothing written there is 0 from whcih we start and at right side it should go to the end
print("numbers after slicing[:5]: ", numbers[:5])  # STARTING FROM O AND GOES TO LESS THAN 5 i.e upto 4th index
print("numbers after slicing[3:]: ", numbers[3:])  # STARTING FROM 3 AND GOES TO END
print("numbers after slicing[3:7}: ", numbers[3:7])  # STARTING FROM 3 AND GOES TO LESS THAN 7 i.e upto 6th index
print("numbers after slicing[:-5]: ", numbers[:-5])  # STARTING FROM O AND GOES TO LESS THAN 5 i.e upto 4th index
# STARTING FROM back and count from 1-5 AND from the 5th index goes to less than -2 i.e.# upto -3rd index
# -- index  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
#   list    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("numbers after slicing[-5:-2]: ", numbers[-5:-2])


print("slicing in list:", data[:2])
print("slicing in tuple :", my_data[:2])
print("slicing in string:", string[:2])
#print("slicing in dictionary:", dict[:2]) --> ERROR
#print("slicing in dict :",dict["name" : "email"] )  --> ERROR -> WITH PASSING KEYS ALSO
#print("slicing in set:", set[:2])   --> ERROR

print()

# CONCATENATION
# in list
data1 = [10, 20, 30]
data2 = [40, 50, 60]
data3 = data1 +data2
print("data3 is :", data3)

# in string
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print("str3 is:", str3)

# in tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print("tuple3 is :", tuple3)

"""
concatenation in string not possible
set1 = {12, 13, 14}
set2 = {15,16,17}
set3 = set1 + set2
print("set3 is :", set3)
"""

"""
concatenation in dictionary not possible

dict1 = {         --> ERROR
    "name" : "john"
}
dict2 = {
    "name" : "jack"
}

dict3 = dict1.append(dict2)
print("dict3 is :", dict3)
"""

print()

# MULTIPLICITY
# list
data4 = data1 * 2
print("data4 is :", data4)

# tuple
tuple4 = tuple1 * 2
print("tuple4 is :", tuple4)

# string
str4 = str1 * 2
print("str4 is :", str4)

"""
-- ERROR
set1 = {1,23,45}
set2 = {34, 32, 24}
set3 = set1 * 2
print("set4 is :", set4)
"""

"""
-- ERROR
dict1 = {
    "name" : "john"
}
dict2 = {
    
    "name" : "jack"
}

dict3 = dict1 * 2
print("dict3 is :", dict3)

"""

print()

# MEMBERSHIP TESTING
# tuple
print("membership testing in tuple")
print(10 in data)
print(1 in data)

# list
print("membership testing in list")
print(10 in data)
print(1 not in data)

# string
print("membership testing in string")
print("h" in string)

# set
print("membership testing in set")
print(100 in set)

# dictionary
print("membership testing in dictionary")
print("name" in  dict)
print("address" in dict)