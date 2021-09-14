"""
    Standardize the Object :)
    WITH IMPROVEMENT
    Making Objects which will have same attributes :)
"""

class Customer:

    # CONSTRUCTOR
    # 1st input is self
    # self is a reference variable
    # it will hold Hash Code of the CURRENT OBJECT
    def __init__(self, name=None, phone=None, email=None, gender=None, address=None):
        print("Constructor Executed")
        print("self is:", self)
        print("type of self is:", type(self))
        print("hashcode of self is:", hex(id(self)))

        # now here values are not fixed,we have passed parameters in the __init__() so the current object
        # has also the same parameters and can change the value if and only iff self has not assigned 'None' to
        # any parameter by accessing it which is shown below.Here self has accessed the parameters and
        # is taking the parameters value.
        self.name_of_customer = name
        self.phone_of_customer = phone
        self.email_of_customer = email
        self.gender_of_customer = gender
        # if u will not access here then it won't be able to take the parameters value
        self.address_of_customer = address

def main():
    # here now we can change the values as parameters are passed in the __init__() and which so ever value
    # is not changed here it will take 'None'
    customer1 = Customer("John", "+91 99999 11111", "john@example", "male", "redwood shoes")
    customer2 = Customer("Fionna")
    customer3 = customer1


    print("customer1:", customer1)
    print("customer1 hashcode is:", hex(id(customer1)));

    print("customer2:", customer2)
    print("customer2 hashcode is:", hex(id(customer2)));

    print("customer3:", customer3)
    print("customer3 hashcode is:", hex(id(customer3)));


    # READ OPERATION
    print("DATA IN OBJECTS NOW: ")
    print(vars(customer1))
    print(vars(customer2))
    print(vars(customer3))

if __name__ == '__main__':
    main()