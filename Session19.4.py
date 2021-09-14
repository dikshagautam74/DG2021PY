"""
 GENERATOR IN PYTHON
 it is basically an object,it yields the data not returns,so func() function now become sa generator
"""

def func():
    yield 10
    yield 20
    yield 30


result = func()
print("result:", result)

# we can print the data in generator that we are yielding with the help of next function.
print(next(result))
print(next(result))
print(next(result))


"""
here you can read a file in generator
----------------------------
def func():


    file = open("Session19.3.py", "r")
    lines = file.readlines()
    for line in lines:
        yield line

result = func()
print("result:", result)

- you can print the line by iterating in generator
# for item in result:
#     print(item)


# we can print the data in generator that we are yielding with the help of next function also.
# it will print one line if you write next() function once.
print(next(result))
print(next(result))
print(next(result))
"""





