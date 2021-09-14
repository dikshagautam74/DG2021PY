from Session14B import LinkedList

class Dish:


    dishes = 0 # property of class

    def __init__(self, name=None, price=None, quantity=None):
        Dish.dishes += 1
        # self contains the HashCode of the Object
        self.idx = -1
        self.name = name
        self.price = price
        self.quantity = quantity

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1

    def __str__(self):
        return "[{index}] | {name} | \t {price} | \t {quantity}".format_map(vars(self))

        # another way to write return statement
        # return "{}\t {}\t{}".format(self.name,self.price,self.quantity)


def main():


    dish1 = Dish("Dal Makhani", 200, 1)
    dish2 = Dish("Paneer Makhani", 300, 1)
    dish3 = Dish("Pizza",100,1)
    dish4 = Dish("Burger",50,1)
    dish5 = Dish("Fries",80,1)


    menu = LinkedList()

    menu.append(dish1)
    menu.append(dish2)
    menu.append(dish3)
    menu.append(dish4)
    menu.append(dish5)

    # printing the length of Linked list in menu with the function length made in Session14B
    print("MENU [{}]".format(menu.length()))
    menu.iterate_forward()

    # getting dish(object) from menu to add in cart
    # to get it executed,pass name arguement in get_object function,it will print u the dish name
    # dish = menu.get_object("Dal Makhani")
    # print("DISH OBJECT DETAILS:", dish)

    # it will print u the dish name by its index
    dish = menu.get_object(1)
    print("DISH OBJECT DETAILS:", dish)

    # u can use this to delete the first element
    #menu.remove_first()

    # calling remove_last() function to delete the last element
    menu.remove_last()
    menu.iterate_forward()

    print()

    # it will delete element at the passed index
    menu.remove(1)
    menu.iterate_forward()




if __name__ == '__main__':
    main()



