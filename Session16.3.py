"""
 Lamba -> Anonymous Function,function without any name
"""

# simple function
def area_of_circle(radius):
    return 3.14 * radius* radius

print(area_of_circle(7))

print()

# lambdas will compute an expression and return the result
# lambda is a function and it takes only input ,it doesn't have any name
ref = lambda radius : 3.14 * radius* radius
# ref = lambda radius = int(input("enter radius:")) :3.14 * radius* radius -> we can take input from user also
print(ref)  # ref has now become a lambda function

print(ref(2))   # it will take input

print()

ref = lambda x = 2, y = 3: x**y
print(ref())  # it will take default value means value already assigned in the function
print(ref(y=2))   # changing the value of y
print(ref(x=3,y=2))

print()

ref1 = lambda x, y: x + y
ref2 = lambda a, b: a * b

# using ref1 and ref2 lambda function in ref3
ref3 = lambda p,q : ref1(p,q) ** ref2(p,q)   # here value to x=p,y=q and a=p,b=q
print(ref3(2,2))   # giving value to p & q

print()

# taking input from user
ref = lambda amount=float(input("Enter Amount: ")), taxes = float(input("Enter Taxes: ")): amount + (amount*taxes)
print(ref())
