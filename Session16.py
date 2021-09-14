# Decorator with parameters

# 1. Outer Function must take function as reference for input
def compute_taxes(func):
    # 2. Create Inner Function
    #    write the logic to decorate
    # u have to give same parameters to the inner function as in pay function
    def inner(amount, taxes):   # u can give here any name to the parameter

        if amount <= 0:
            print("This is an Invalid Amount")
            return                  # terminate the inner function -> iske aage jo bhi likha h vo nhi chlega

        elif amount > 0 and amount < 2000:
            taxes = 0.18

        elif amount >= 2000:
            taxes = 0.25

        print("hello")

        # 3. Execution of the Function which was passed as input
        func(amount, taxes)

    # 4. return inner function
    return inner


# @compute_taxes
def pay(amount, taxes):
    print(amount + (taxes*amount))

# pay(1000,0.10)

# here we are assigning pay function not executing so we will write pay without ()
result = compute_taxes(func=pay)
result(0, 0.10)



