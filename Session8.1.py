class customer:

    # 1st input(parameter) is self
    # self is a reference variable
    # it will hold Hash Code of the CURRENT OBJECT
    # __init__ is a CONSTRUCTOR
    def __init__(self):
        print("self is :", self)
        print("type of self is :", type(self))
        print("hash code of self is :", hex(id(self)))

        # once u have assigned the value like here 'None' is assigned to all the attributes
        # same will be copied to the objects made further(i.e.customer1),u can't change it's value
        # it will print u 'None' when u apply "vars()" function
        self.name = None
        self.age = None
        self.phone = None
        self.email = None




def main():
    # if u try to modify the value here like     customer1 = customer("robin","12") it will give u error
    # because we have only passed self as a parameter in the __init__(),if have passed "name","age",etc..
    # as parameters then it will not give error but still it will not change the value bcoz we have
    # assigned 'None' to all the attributes
    # see next program for the modification
    customer1 = customer()
    print("customer1 is :", customer1)

    print(vars(customer1))

if __name__ == '__main__':
    main()