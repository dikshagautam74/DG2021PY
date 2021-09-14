# RECURSION -> function repeating itself just like a loop
# we need to execute the same function from itself

# this is a for loop which works in repetition , now we have to make recursive function
# here we are starting from 10 and ending at 0 , decrementing i by 1
#for i in range(10, 0 ,-1):
#    print(i)

def recursion(num):
    if num < 1:
        return
    else:
        print(num)
        num -= 1
        recursion(num)          # recursion() func. is repeatedly executed

# this recursion(data) execution has been starting from the main function
data = 10
recursion(data)

