"""
If/else
"""

promo_codes = {
    "NOCOOKING": {
        "min":159,
        "discount":0.50,
        "upto":100
    },
    "WELCOMEPTM": {
        "min": 299,
        "flat": 75
    }
}

amount = int(input("Please enter the amount"))
promo_code = input("Enter the promo code")

print("amount is:",amount)
print("promo code is:",promo_code)

if promo_code in promo_codes:
    print("VALID")

    promo_code_info = promo_codes[promo_code] #promo_code_info has given the access of promo_code from promo_codes

    if "discount" in promo_code_info:
        print("PERCENTAGE DISCOUNT")
        print("discount in percentage is:",promo_code_info["discount"])

        if amount >= promo_code_info["min"]:
            discount = amount * promo_code_info["discount"]

            if discount > promo_code_info["upto"]:
                amount -= promo_code_info["upto"]
                print("Amount after percentage discount is :",amount)
            else:
                amount -= discount
        else:
            print("Amount is Lesser. Please add items worth \u20b9", (promo_code_info['min'] - amount), "more")
    else:
        print("FLAT DISCOUNT")
        print("flat discount is:", promo_code_info["flat"])
        amount -= promo_code_info["flat"]
        print("amount after flat discount is :",amount)

else:
    print("INVALID")

print("Please Pay:",amount)