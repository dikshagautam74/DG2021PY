"""
 datetime is a built-in module
 today is a builtin function
"""

# another way to write import statement
# import datetime as dt
# today = dt.datetime.today()

#  importing only date from datetime module
# from datetime import date
# today = date.today()

#  importing only time from datetime module
# from datetime import time
# today = time.today()

import datetime
# here these are builtin          module   class    fucntion
#                         today = datetime.datetime.today()

today = datetime.datetime.today()
print("Today :", today, type(today))

# convert today into string type
today = str(today)
print("Today now is :", today, type(today))

# split the date and time
today = today.split()
print(today[0])
print(today[1])


today = datetime.datetime.today()
# giving arguments to print the tomorrow's date and time
tomorrow = datetime.datetime(2021, 8, 14, 13, 00)
print("tomorrow:", tomorrow)

# difference of tomorrow and today
print(tomorrow - today)




