# STRINGS AND SOME OF ITS FUNCTIONS


restaurant = 'Famous Bakers'
print(restaurant)
print("length:", len(restaurant))
print("max:", max(restaurant))    # it will print max according to ascii value
print("min:", min(restaurant))    # -> this will print me a space

# writing liking this('s) in single inverted commas will give error
#restaurant = 'Famous Baker's'

# writing liking this('s) in double inverted commas will not give error
restaurant = "Famous Baker's"
print(restaurant)

# to remove apply backslash
restaurant = 'Famous Baker\'s'
print(restaurant)

# we can make a string like this also
print("""--------------
Please be seated
--------------""")

# Raw(r) Strings are Used with Regular Expressions -> whatever expression(-,=,\,etc) are in string
# it will print as it is by applying r before the string
restaurant = r'Famous Baker\'s'
print(restaurant)

# Property -> Strings are immutable
# Strings cannot be modified.
# Any manipulation on String will create a new String in Memory
names = "robin, benny, jack, jim, jack"
print("names:", names)

# convert all aphabets into uppercase
new_names = names.upper()
print("new_names:", new_names)


# convert first alphabet of first word in capital
capitalize_names = names.capitalize()
print("capitalize_names:", capitalize_names)

# here u can see 'names' string is not modified
print("names string is immutable:", names)

# convert first alphabets of all the word in uppercase
print("using title:", names.title())

# works same as upper()
print("using swapcase():", names.swapcase())

# strip() function removes all the starting and ending whitespaces
password = input("Enter Password: ").strip()

# rstrip() removes all the whitespaces from right
#password = input("Enter Password: ").rstrip()

# lstrip() removes all the whitespaces from left
#password = input("Enter Password: ").lstrip()

# inputing '   hello   ' and using strip() will remove the whitespaces from both left and right and print us 'hello'
print("password is:", password)

data = "00000034500"
print(data.strip("0"))    # remove all the zeroes
print(data)

print()

message = "hello people"
print(message.center(60))    # shifts to the center 30 from left and 30 from right
print(message.ljust(60))
print(message.rjust(60))

print()

# right shift string with 10 spaces and with '-' this sign
print("345".rjust(10,'-'))

# fills zero to make a 10 digit no. string
print("345".zfill(10))

print()

quote = "search the candle rather than cursing the darkness"
print(quote.find("sing"))
print(quote.index("the"))
print(quote.rindex("the"))  # finds index of "the" starting from right but count the index from left only

print()

names = "robin, benny, jack, jim, kat"
print(len(names))
# indexing
print(names[len(names)-3])

split_names = names.split()
print(split_names)
split_names = names.split(",")
print(split_names)

print()

# in this, names to the left and right side of jim are included in a separate string
partitoned_names = names.partition("jim")
print(partitoned_names)

print()

for ch in names:
    print(ch, end=" ~ ")

print()

print("names:", names.replace("benny","jenny"))

contacts = {
    "harry",
    "benny",
    "robin",
    "jim",
    "jack",
    "kat",
    "rojh"
}

search_keyword = input("Search:")
print("Search keyword:", search_keyword)


for contact in contacts:
    # if the inputted search keyword is in contacts,then those contacts will be printed
     if contact.lower().__contains__(search_keyword.lower()):
         # if the contacts starts with the inputted search keyword, then it will print those contacts
    #if contact.lower().startswith(search_keyword.lower()): # endswith
        print(contact)

print()

name = "robin"
age = 20
email = "robin@anything.com"

# 3 ways for printing the details
# keep paranthesis empty
print("Details for {}\n{} | {}".format(name, age, email))

# put index in  paranthesis
print("Details for {0}\n{1} | {2}".format(name, age, email))

print("Details for {first}\n{second} | {third}".format(first = name, second = age, third = email))

print()

bill_amount = 120.54311
# slicing
print("Bill is: {:.3f}".format(bill_amount))    # starts from 0 index and goes to 3 floating number
