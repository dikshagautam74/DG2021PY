menu = {
    "brand1" : {
    "name": "H&M",
    "price":3000
    },

    "brand2" : {
    "name": "NIKE",
    "price":2500
    },

    "brand3" : {
    "name": "PUMA",
    "price":2000
    },

    "brand4" : {
    "name": "ALDO",
    "price":4000
    },

    "brand5" : {
    "name": "ZARA",
    "price":1500
    }
}

print("MENU")
keys = list(menu.keys())

for key in keys:
    print("-"*20)
    print("{}\t\t \u20b9{}".format(menu[key]["name"],menu[key]["price"]))
    print("-"*20)
    print()

shopping_cart = []
total = 0

while True:
    choice = input("Enter the brand to buy: (no to quit)")
    if choice == "no":
       break

    if choice in menu:
       total += menu[choice]['price']
       shopping_cart.append(menu[choice])

    else:
       print("Sorry!We do not have this",choice,"at the moment")

print("SHOPPING CART [{}]".format(len(shopping_cart)))
print("Please Pay [\u20b9{}]".format(total))
print(shopping_cart)







