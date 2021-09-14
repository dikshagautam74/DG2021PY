import db
from db import dbOperations


print("Welcome to Session20F")
print("Name of Session20F is:", __name__)
print()
print(db.message)

dbOperations.add()

"""
 Another way to write the above same program
 
from db import *
from db import dbOperations


print("Welcome to Session20F")
print("Name of Session20F is:", __name__)
print()

print(message)
# print("DB Name is:", db.message)

dbOperations.add()"""