"""
Value vs Reference
"""

a = 10
# here value of a is assigned to b
b = a  #reference copy -> Single value container

print("a is : ",a , "hash code is :",hex(id(a)))
print("b is : ",b , "hash code is :",hex(id(b)))

# Manipulation results in new object in memory -> means value of b has changed
# hence , b will refer to a new object
b += 5

print("a now is : ",a , " hash code is :",hex(id(a)))
print("b now is : ",b , " hash code is :",hex(id(b)))

