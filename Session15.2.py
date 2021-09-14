"""

  VARIABLE ARGUEMENTS -> *args
    it takes as many arguements we want to give

  KEYWORD ARGUEMENTS -> **kwargs

"""

# def add_numbers(*args)
# def add_numbers(*kuch_bhi_naam_ho_skta_hai)


def add_numbers(*numbers):
    print("Numbers are :",  numbers)
    print("Type of numbers:",type(numbers))
    print("Sum of numbers :",sum(numbers))
    print()

add_numbers(10, 20, 30)
add_numbers(10, 20, 30, 40, 50)
add_numbers(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#add_numbers(10, 20, 30, 40, "fifty", 60, 70, 80, 90, 100) -> write 50 as "fifty" will not give ERROR as tuple can hold different data types


def add_numbers(numbers):
    print(numbers)

#add_numbers(10,20,30)   -> ERROR as numbers will take only 1 arguement and here 3 are passed

add_numbers(numbers=(10,20,30))   ## we can pass (10,20,30) to numbers like this and it will not give ERROR

print()

# **kwargs takes arguements with keyword mentioned
def plot_graph(**options):
    print(options)
    print(type(options))

# keyword should not be in inverted commas
plot_graph(color = "red", x = 10,y = 20, type = "line")

print()

def fun(*args,**kwargs):
    print("args is:",args,type(args))
    print("kwargs is:",kwargs,type(kwargs))

# we can't pass arguements in reversed order like fun(kwargs,args)  --> it will give ERROR
# fun(x = 1, y = 2, z = 3,10, 20, 30)

# it will take args and kwargs from this
fun(10, 20, 30, x = 1, y = 2, z = 3)

