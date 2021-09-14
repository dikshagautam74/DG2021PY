"""
 This is documentation comment -> should always be in the beginning
 This is session 2 in which we learn model
 here we see single value and multi value containers

   Student : Diksha
   Course : Python
   Age : 20
   Date : 19th July,2021
   Teacher : Ishant kumar
"""

#THIS IS A COMMENT

# __doc__ is a magic variable to see documentation of python module/script
print(__doc__)

"""
  MODEL
  1. Single value container -> holds a single value
  2. Multi value container  -> holds multiple values
    2.1 Homogeneous -> values of same type
    2.2 Heterogeneous -> values of different type
    
"""

# create a single value storage container in RAM
# store 10 in it which is equal to a
# put the hash code of 10 in a like a has address like for eg. 1001
# so now, a is a reference variable which will hold the hash code of 10
# this technique works like a pointer

# CREATE
a = 10
b = 20

# READ
# TYPE will tell the data type of value stored in variable
# hex converts the id into hexical value and same as with octal and binary
print(" a is : ",a, type(a), id(a), hex(id(a)),oct(id(a)),bin(id(a)))
print(" b is : ",b, type(b), id(b), hex(id(b)),oct(id(b)),bin(id(b)))

#  UPDATE
a = 30.2
print(" a now is : ",a, type(a), id(a), hex(id(a)),oct(id(a)),bin(id(a)))
print(" b now is : ",b, type(b), id(b), hex(id(b)),oct(id(b)),bin(id(b)))



# DELETE -> this will give error as "a is not defined" means now a is deleted
#del a
#print(" a is : ",a, type(a), id(a), hex(id(a)),oct(id(a)),bin(id(a)))

# STORING MULTIPLE VALUES
numbers1 = 10,20,30,40,50
numbers2 = 10.34,20.1,30,40,50.6

# here TYPE will be TUPLE which says multiple values stored in a variable
print(numbers1 , type(numbers1))
print(numbers2,type(numbers2))

