"""
 class and object
"""

class dish:

    # property of class
    dishes = 0
    print("dishes:", dishes)


    def __init__(self,name = None, price = None):
        # self.name and self.price are property of object
        self.name = name
        self.price = price

         # using class variable i.e. dishes, we don't have to give dishes as a parameter to __init__
        # it's value will automatically be added in all the objects
        # self.dishes = 1

        # it is used to calculate the objects
        # working -> whenever the object gets executed, it comes here, it's value got stored in it.
        dish.dishes += 1


def main():
    dish1 = dish("pizza", 200)
    dish2 = dish("burger", 100)
    dish3 = dish("fries",50)

    # when we write like this,our dishes attribute will not get incremented
    dish4 = dish1

    # dishes is a class variable which is accessed here with the help of class and we have changed it's value
    # it got printed in class's attributes
    # dish.dishes = 100

    print("data for dish1: ", vars(dish1))
    print("data for dish2: ", vars(dish2))
    print("data for dish3: ", vars(dish3))
    print("data for dish4:",  vars(dish4))

    print("data for class dish :", vars(dish))



if __name__ == '__main__':
    main()