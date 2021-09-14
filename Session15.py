"""
  Functions
"""

def add_numbers(num1,num2):
    result = num1 + num2
    print("result is:", result)


# giving default values to the arguements should start from right side i.e. from packing charge to the left
# beech mein se value nahi de sakte like taxes ko 0 de dia aur packing charge & delivery fee ko kuch nhi
# it will give error
# def calculate_bill_amount(amount,taxes = 0,delivery_fee , packing_charge ) -> ERROR
# def calculate_bill_amount(amount,taxes = 0.10,delivery_fee = 0, packing_charge): -> ERROR
def calculate_bill_amount(amount,taxes = 0.10,delivery_fee = 0, packing_charge = 0):
    total = amount + (0.6*taxes) + delivery_fee + packing_charge
    print("total is:", total)


# calling function and giving values to the arguements
add_numbers(1,2)

# -> assigning value to amount is compulsory as we haven't passed it a default value in the function.
# rest other parameters are passed a default vaule,so if we don't give them value in calling it will not give ERROR
calculate_bill_amount(amount=2000)
calculate_bill_amount(amount=2000,delivery_fee=100)
calculate_bill_amount(packing_charge=50,amount=2000)
calculate_bill_amount(packing_charge=50,amount=2000,taxes=5)


# reference copy
fun1 = add_numbers


# these are 2 ways to execute a function which will give the same result
# 1.only give values
fun1(1,4)
# 2. assign values using arguement name
# fun1(num1=1,num2=4)
