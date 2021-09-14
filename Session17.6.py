"""
  Some OOPS concepts -> class and object
"""

class User:
    def __init__(self,name,roll,age):
        self.Name = name
        self.Roll = roll
        self.Age = age

    def show(self):
        print("user details:", self.Name, self.Roll, self.Age)



def main():
    user = User("john", 12, 5)

    # Method 1 -> to print the details of user
    # print(vars(user))

    # Method 2
    # accessing show function with the help of object
    # user.show()     -> this is translated into "User.show(user)"

    # Method 3
    # accessing show() with the help of a class and passing object as an arguement
    User.show(user)

if __name__ == '__main__':
    main()