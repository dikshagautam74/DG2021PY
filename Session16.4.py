"""
  MAP  -> map function will do mapping
  FILTER  -> filter the elements according to our condition
  REDUCE
"""

# this statement is used for reduce function so that we can use it.
from functools import reduce

# SIMPLE IMPLEMENTATION OF FUNCTION AND LAMBDA FUNCTION
product_prices = [1000, 2000, 6000, 11000, 5000, 4500, 9800, 14600]

# 2nd way to calculate discount on product prices using function with parameters
def cal_discount_on_price(amount, discount=0.50):
    return amount - (amount*discount)

# 3rd way to calculate discount on product prices using lambda function
cal_discount = lambda amount, discount: amount - (amount*discount)



# 1st way to calculate discount on product prices using for loop
for price in product_prices:
    print("Original Price :", price)

    # it will calculate discount on price using for loop
    print("Price after discount:",price - (0.25 * price))

    # here the function is called,and got printed what the function is returning i.e. discount on price
    print("Price after discount:", cal_discount_on_price(price,0.25))

    # it will calculate discount on price using lambda function
    print("Price after discount:", cal_discount(price,0.25))
    print()


# ---------------------------------------------------------------
# MAP FUNCTION IMPLEMENTATION  -> IT SAVES TIME , IT'S A ONE LINE CODE WITH THE HELP OF LAMBDA FUNCTION.

# this is iterable part
product_prices = [1000, 2000, 6000, 11000, 5000, 4500, 9800, 14600]

# this is function that map takes as 1st arguement,in amount arguement value of product prices go one by one
# and the result calculated returned to the map function
def cal_discount_on_price(amount):
    return amount - 100

# MAP  -> takes 2 arguements -> (func,iteratable)  -> iteratable means list,tuple,set,dictionary
result = list(map(cal_discount_on_price,product_prices))

# passing lambda function directly as a function arguement
# result = list(map(lambda amount : amount - (0.50 * amount),product_prices))

print("result after mapping is:", result)


"""

product_prices = [1000, 2000, 6000, 11000, 5000, 4500, 9800, 14600]

# here if u give 2 arguements to the function,u have to assign value to the discount arguement where the
# function is defined as the product prices will get confused that to whom the value should be assigned.
def cal_discount_on_price(amount,discount=100):
    return amount - discount

# using lambda function in function arguement
cal_discount = lambda amount, discount=0.50: amount - (amount*discount)

# result = list(map(cal_discount_on_price,product_prices))
result = list(map(cal_discount,product_prices))

print("result is:", result)"""

# -----------------------------------------------------------
# FILTER FUNCTION IMPLEMENTATION

# it will give the elements greater than 5000 and this is konown as filteration.
result = list(filter(lambda amount : amount > 5000,product_prices))
print("Filtered result:", result)

# -----------------------------------------------------------
#  REDUCE FUNCTION IMPLEMENTATION

shopping_cart = [1000,4000,2500]

# working of reduce function -> to use reduce function we have to write import statement
# Step 1. value of 1000 goes into x and 4000 goes in y , then the add operation is performed and they got added
# It will return 5000 after addition
# Step 2. Now 5000 goes into x and 2500 goes in y,and again add operation is performed
# Now it return the final result i.e. 7500
amount_to_pay = reduce(lambda x, y: x + y, shopping_cart)
print("amount to pay :", amount_to_pay)







