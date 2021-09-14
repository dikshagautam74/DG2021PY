"""
CONTROLLER -> makes the algorithm
  1. Computation -> Operators
  2. Logical Decisions -> if-else , switch case(not used in python)
  3. Iterations -> for,while

"""

# ARITHMETIC OPERATORS :  +, -, *, **, /, //, %
num1 = 1
num2 = 2
num3 = num1 + num2

num4 = num1/num2         #single division gives floating point division
print(num4)
num4 = num1//num2       #double division gives integral division
print(num4)

#HASHING
#hashfunction(data) -> hash code
#buckets = 13
# h(x) = x % buckets   -->> gives remainder on division

bucket_size = 13
number = 100
hash_code = number % bucket_size
print("hash code is : ",hash_code)

result = 3**2    # ** -> it works as exponential like in this it is 3^2
print("result is : ",result)

#ASSIGNMENT OPERATORS : +=,-=,*=,**=,/=,//=,%=
quantity = 20
quantity += 2   # here quantity becomes 22
quantity %= 3   # here quantity becomes 1 as 22/3 gives remainder 1
print(quantity)

#CONDITIONAL OPERATORS -> >,<,>=,<=,!=

e_wallet = 300
cab_fare = 400
#  here condition is applied to cabfare and wallet
print("can i book a cab?",cab_fare < e_wallet)   # returns false as 400>300

# LOGICAL OPERATORS -> and,or,not
internet = True
gps = False
# condtion checked with and operator
print("can i navigate on google maps? ",(internet and gps))

# is and is not operator
print(e_wallet is cab_fare)   # it checks if both comparators are equal or not,if equal then returns true
print(e_wallet is not cab_fare)

#BITWISE OPERATORS -> &,|,^  ->> works on bits(0,1)
num1 = 8
num2 = 10
# for 8 = 1000
# for 10= 1010
# 8 & 10= 1000

print("binary conversion of num1 is : ",bin(num1))
print("binary conversion of num2 is : ",bin(num2))

num3 = num1 & num2
print("binary conversion of num3 is : ",bin(num3))
print("num3 is : ",num3)

num4 = num1 | num2
print("binary conversion of num4 is : ",bin(num4))
print("num4 is :",num4)

# 8  = 1000
# 10 = 1010
# 8^10=0010
num5 = num1 ^ num2
print("binary conversion of num5 is : ",bin(num5))
print("num5 is :",num5)

#SHIFT OPERATORS -> RIGHT SHIFT(>>) , LEFT SHIFT(<<)
num1 = 8

num3 = num1 >> 3   #divide num1 by 2 power n means 2^3 in right shift
print(num3)
num3 = num1<< 3    #multiply num1 by 2 power n means 2^3 in left shift
print(num3)

"""
 we have to do -> -11>>2
 for that                    11 ->  1011
                             1's -> 0100
                             2's ->   +1
                             -11 -> 0101
         right shift means discard the bits as given from the right
         like in this eg,it is right shifted by 2,so we'll remove 01 from the right side
         and the remaining 01 at the left gets shifted to the right and at the place of them
         we'll add 1(only when we have -ve no. otherwise 0)                    
       empty first 2 places  >>2 -> __01
         place 1 in these places -> 1101
                    again do 1's -> 0010
                            2's  ->   +1 
                                    0011  -> -3 


"""

num1 = -13
num2 = 3
result = num1>>num2
print("result is :",result)

# MEMBERSHIP TESTING -> in,not in
data = [10,20,30]
print(10 in data)   # it checks whether 10 is in our data or not
print(100  in data)