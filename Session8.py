"""
    Studying OOPS in python
    in python, we can make different objects of one single class
"""

# CLASS CREATION
class customer:
    pass

class restaurant:
    pass

class menu:
    pass

class dish:
    pass

# Main function to execute the App
def main():
    # OBJECT CONSTRUCTION STATEMENT
    robin = customer()  # robin is a reference variable of class customer,customer is an object
    jack = customer()  # jack is an reference variable of class customer,customer is an object
    customer3 = customer()  # jack is an reference variable of class customer,customer is an object

    # REFERENCE COPY
    customer4 = robin

    print("robin is :", robin)
    print("jack is :", jack)
    print("custumer3 is :", customer3)
    print("custumer4 is :", customer4)

    # this __dict__ attribute used to store object's attributes
    #print(robin.__dict__)
    #print(jack.__dict__)
    #print(customer3.__dict__)

    # vars() function prints us the variable arguement present in the object
    # here for now we don't have stored any object's attributes,so it will print empty paranthesis i.e. {}
    print(vars(robin))
    print(vars(jack))
    print(vars(customer3))

    print()

    # 1. WRITE DATA
    robin.age = "10"
    robin.email = "robin@example.com"

    jack.age = "12"
    jack.email = "jack@example.com"

    customer3.name = "john"
    customer3.email = "john@example.com"
    customer3.phone = "+91 94534 35678"

   # 2. UPDATE DATA
    customer4.age = "15"

    # 3 . DELETE OPERATION
    del customer3.phone     # it will delete customer3's phone number

    # 4. READ OPERATION
    # now here we have written the data in all the objects,now vars() function will print these attributes
    print(vars(robin))
    print(vars(jack))
    print(vars(customer3))
    print(vars(customer4))



if __name__ == '__main__':
    main()