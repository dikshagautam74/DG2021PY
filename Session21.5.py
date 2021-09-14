# different import statements

"""
 '*' means all  i.e. from Session21C import all
"""

from Session21C import *

print()

show()
print("name of the imported session:", name)  # here u don't have to write Session name to print the name


# object made of class
ref = training()
# ref.fun()   # accessing fun of class

print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
 u can import attributes by their name also

"""
from Session21C import name, show, training

print(name)
print(show())

ref1 = training()
ref1.fun()
print(ref1)
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
 here n is an alias name for 'name' attribute , now u can write 'n' instead of writing 'name' 
"""

from Session21C import name as n

print(n)
show()
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
 here Class is an alias name for 'training' class , now u can write 'Class' instead of writing 'training'
"""

from Session21C import training as Class

ref2 = Class()
ref2.fun()
print(name)    # here u can directly print name without writing Session name becoz a import statement is written with *.

