class Dish:

    dishes = 0    # property of class

    # Constructor
    """
    def __init__(self, price=None, quantity=None):
        # self contains the HashCode of the Object
        
         -> we can take input from user and we don't hacve to take parameter in constructor and it works same
        self.name = input("Enter Dish Name: ")  
        self.price = price
        self.quantity = quantity
    """

    def __init__(self,name = None,price = None,quantity = None):
        self.name = name
        self.price= price
        self.quantity = quantity

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1



def main():
    dish1 = Dish("pizza",200,1)
    dish2 = Dish("burger",100,1)
    dish3 = dish1

    print(vars(dish1))
    print(vars(dish2))
    print(vars(dish3))
    print(vars(Dish))   # data of Dish class

    print()

    Dish.dishes += 1

    dish1.increment()
    dish2.increment()
    dish3.increment()   # when we increment quantity in 3 it also increments in 1

    dish1.increment()
    dish3.increment()

    dish2.increment()
    dish1.decrement()   # decrement will decrease the quantity by 1


    print(vars(dish1))
    print(vars(dish2))
    print(vars(dish3))
    print(vars(Dish))    # data of Dish class after increment



if __name__ == '__main__':
    main()



