"""
MODEL
   single value container -> int , float, string
   multiple value container -> tuple,array,list,dictionary,sets

VIEW
  always works with strings
  Textual interface -> means it will give string type only  of any type(int,float,etc) variable

"""


print("hello,What's your name?")

# take input from user
name = input("We want to know your name.Please can you tell?")
print(name,type(name))

# as age is of "int" type ,it will print "string" type bcoz of textual interface
# we can convert it in "int" by writing it as -> age = int(input("enter your age"))

age = int(input("enter your age"))
print(age,type(age))


