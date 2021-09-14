"""
   Regular Expressions
   Flexible pattern matching technique
"""

import re

# regex is a string,you can give any name here ; \s+ is for whitespaces
regex = re.compile("\s+")
print("regex:", regex, "type of regex:", type(regex))

print()

quote = "Search the Candle rather than cursing the Darkness"
print(quote)
result = regex.split(quote)
print("result after splitting:", result)

print()

contact_names = ["      ", "john", "jennie   ", "   george  "]
for name in contact_names:
    if regex.match(name): # will match name having whitespaces from beginning
        print("Pattern Matched For", name)
    else:
        print("Pattern NOT Matched For", name)


print()

regex = re.compile(""
                   "")
result = regex.split(quote)
print(result)

print()

data = regex.search(quote)
print(data)
print(data.start())

print()

# replacing 'the' with 'will' in the quote with repace() func.
new_quote = quote.replace('the', 'will')
print("quote:", quote)
print("new_quote:", new_quote)

print()


message = "This is a good day. is it going to rain ?"
# pattern changed, now it is 'is'.
regex = re.compile("is")
results = regex.findall(message)      # finds 'is' in the message
print(results)

print()

# it is a snippet which ensures that email entered is correct
email = input("enter the email")
print("you entered:", email)
# u can use bool var also
#flag = True   -> this means that the above 2 lines are true
for i in range(len(email)):
    if email[0] == '@':
        print("invalid")
        #flag = False     -> this means that the above  lines are false
    if email[0] == '.' or email[1] == '.':
        print("invalid")
        #flag = False

email_regex = re.compile("\w+@\w+\.[a-z]{3}")

# using the pattern find all the things in the email entered,if the email is correct,then it will print us the email
# otherwise print us  this -> '[]'
result = email_regex.findall(email)
print(result)

message = "please pay $100"
# \w+ is a pattern in regular expression which gives the following alphabets those are wriiten with for eg '$'
# in this code, it will give '$100' as 100 is wriiten with $
regex = re.compile("\$\w+")        # -> we can write like this also regex = re.compile("\\$\\w+")
print(regex)
print(regex.findall(message))

print()

# in this,in b/w where ever we find digits from 0-9 it will get printed
message = "I have been vaccinated 2 times. I am 12 years old. i feel more safer"
regex = re.compile("[0-9]")
result = regex.findall(message)
print(result)

print()

# it will start from beginning and find first character as alphabet and second as digit
regex = re.compile("[A-Z][0-9]")
data = "108AB, PB, HP, C6, 55,G7"
results = regex.findall(data)
print(results)

print()

message = "I have a 2 wheeler vehicle.Registration no. is PB10AL2937"
# [A-Z]{2] MEANS THE PATTERN HAVING FIRST 2 CHARACTERS ARE ALPHABETS AND ||LY WITH DIGITS
regex = re.compile("[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}")
print(regex.findall(message))