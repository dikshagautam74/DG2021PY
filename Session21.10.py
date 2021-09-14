# built in module random
import random

# here randrange is a built in function,which takes 3 arguements that otp should be in range from 0-100000
# otp will take any random value b/w the mentioned range,it's ur choice to give 3rd argument(step) or not.
otp = random.randrange(100000)
print("1. OTP :", otp)

# here the arguments are given from 1000-2000
otp = random.randrange(1000, 2000)
print("2. OTP :", otp)

# here the range is from 100-200 and the otp it will give,it gets incremented by step 1.
otp = random.randrange(100, 200, 1)
print("3. OTP :", otp)

# it takes 2 arguements only,and the range is from 111-222
otp = random.randint(111, 222)
print("4. OTP :", otp)