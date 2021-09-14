
"""
    DECORATORS
"""

def buy_burger(make_a_meal=False, meal=None):
    if make_a_meal:
        def make_burger_a_meal():
            print("Burger Ordered :)")
            print("Upgrading the Burger to a Meal....")
            meal

        return make_burger_a_meal
    else:
        def make_burger_without_meal():
            print("Burger Ordered Without any Meal :)")

        return make_burger_without_meal

@buy_burger
def burger_with_veg_meal():
    print("An Upgrade to Burger with Veg Meal")
    print("Additional Drink and Fries")


@buy_burger
def burger_with_non_veg_meal():
    print("An Upgrade to Burger with Non Veg Meal")
    print("Additional Drink, Fries, Chicken Pop Corn")


burger_with_non_veg_meal()
burger_with_veg_meal()



# result = buy_burger(make_a_meal=False, meal=burger_with_non_veg_meal)
# result()


