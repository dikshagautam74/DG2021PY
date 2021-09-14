
# we can also create main function in python
# def any_name_for_main():

# this will print the name of the function -> i.e __main__
print(__name__)

# this code will not get executed until mainy() is called.Code other than this will executed first
def mainy():
    print("hi")
    a = 10
    data = [10, 20, 30, 40, 50]
    print("This is main")

print("bye")

# code will start running from here and after the mainy() called then it goes to the above code
# this is the condition to check whether the function is main() or not

if __name__ == "__main__":
    print("hy")
    mainy()
