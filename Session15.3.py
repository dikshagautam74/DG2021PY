"""
   PASS FUNCTIONS AS ARGUEMENTS
   RETURNING FUNCTIONS FROM FUUNCTIONS
   NESTED FUNCTIONS

"""

def welcome():
    print("Welcome")

def home(any):

    print("This is function home")

home(any = welcome())   # write like this also home(welcome())

print()

# THIS IS ALSO A WAY TO PASS FUNCTION AS ARGUEMENT
# header = welcome()   -> passing function to a variable
# home(header)         -> pass that variable as an arguement  this can also be written as home(any = header)

"""
another way to pass function as arguement
def home(any):
    any()
    print("This is function home")


home(welcome) / home(any = welcome)
"""

# RETURNING FUNCTION FROM A FUNCTION
def hello():
    return welcome()

hello()

"""
Another way to call function
result = hello()
result()
"""

print()

# NESTED FUNCTIONS
def outer():
    print("this is from outer")


    def inner():
        print("this is from inner")


    inner()

    """
    another way to return inner
    inner()
    return inner
    """
     #  another way
    # return inner()  # without writing this line ,inner() print statement will not be executed


outer()


