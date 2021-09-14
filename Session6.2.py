"""
Functions -> can be created anywhere
Methods -> created inside a class

y = x*x + 1
f(x) = y

function is a piece of logic, which can be executed again and again
When we are writing the same code snippets again and again we need functions
A function is created with def keyword in python
"""

# Defining a function
def f(x):
    y = x*x + 1
    print("y is :", y)

# Execution
# value of x is putted in function
f(1)
f(10)

print("f is :", f, "hash code is:", hex(id(f)))

my_fun = f      # Reference copy
print("f is :", my_fun, "hash code is:", hex(id(my_fun)))
my_fun(3)

#here by using function we don't have to write the code again and again
def find_max(data):

    max = data[0]

    for number in data:
        if number > max:
            max = number

    #return max

marks = [75, 80, 50, 60, 88]
heights = [155, 145, 165, 135, 120, 133, 102, 121]
roll_no = [12, 10, 50, 43, 32, 27]

# here the value will get stored in max and by writing max(marks) will print the max marks
print("Maximum marks is :",max(marks))
print("Maximum heght is :",max(heights))
print("Maximum roll no. is :",max(roll_no))

"""
this is another way to print the maxinimum with the help of function
print("Maximum marks is :",find_max(marks))
print("Maximum heght is :",find_max(heights))
print("Maximum roll no. is :",find_max(roll_no))
"""

"""
this is one way to find max without using function
# Assume
marks = [75, 80, 50, 60, 88]
heights = [155, 145, 165, 135, 120, 133, 102, 121]
roll_no = [12, 10, 50, 43, 32, 27]

here we have to write the code again and again for marks,heights,roll no.
max = marks[0]
for number in marks:
    if number > max:
        max = number
print("max marks is:", max)

max = heights[0]
for number in heights:
    if number > max:
        max = number
print("max heights is:", max)

max = roll_no[0]
for number in roll_no:
    if number > max:
        max = number
print("max  roll no. is:", max)
"""








