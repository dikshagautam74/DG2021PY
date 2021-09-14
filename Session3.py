# DYNAMIC TYPING -> in this ,same variable can hold different types
# in this eg, "name" has different types


name = "jumbo"
print(name, type(name),hex(id(name)))

name = 10
print(name, type(name),hex(id(name)))

name = 20.45
print(name, type(name),hex(id(name)))

name = 10,20,30,40,50
print(name, type(name),hex(id(name)))