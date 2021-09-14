class Menu:
    def __init__(self, name, dishes, num_of_dishes):
        self.name = name
        self.dishes = dishes
        self.num_of_dishes = num_of_dishes

class dish:
    dishes = []

    def __init__(self, id, name,price):
        self.id = id

        self.name = name
        self.price = price


    @classmethod
    def generate_dishes(cls):
        file = open("dishes.csv", "r")
        lines = file.readlines()
        for line in lines:
            data = line.split(",")

            ref = cls(int(data[0], data[1], float(data[2]))
            ref.dishes = cls.dishes
            # cls.dishes.append(ref)

            dishes.append(ref)

        return dishes


def main():
    dish.generate_dishes()



    menu = Menu(name="Veg Indian Menu", dishes=dish.dishes, num_of_dishes=len(dish.dishes))

    for dish1 in dishes:
        print(vars(dish))



if __name__ == '__main__':
    main()