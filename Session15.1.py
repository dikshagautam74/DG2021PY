"""
 RE-DEFINING A FUNCTION
"""
def add_numbers(num1,num2):
    sum = num1 + num2
    print("sum of 2 inputs is:",sum)


print("hashcode of add_numbers:", add_numbers)

# RE DEFINE add_numbers() with 3 inputs will remove the predefined add_numbers() with 2 inputs from memory
def add_numbers(num1=10,num2=20,num3=30):
    sum = num1 + num2 + num3
    # sum = num1 + num2   -> we can do like this also
    print("sum of 3 inputs is:",sum)

# CALLING
# add_numbers(1,2,3)
print("hashcode of add_numbers now is:", add_numbers)  #-> here hashcode will be different now
#
# print("-"*10)

# calling add_numbers by giving 2 inputs will give the output of 3 inputs as it will take num3's default value
# passed in the function ,it will not print for 2 inputs as add_numbers() with 2 inputws is removed now
# from the memory
add_numbers(20,30)

print()

def show():
    print("Hello people")

show()

# RE DEFINE
def show(name):
    print("Hello people.My name is:",name)

show("john")