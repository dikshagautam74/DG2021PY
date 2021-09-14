# 2 ANOTHER EXAMPLE OF DECORATORS WITH ARGS AND KWARGS PARAMETERS

# HERE IN 1st EXAMPLE,WE ARE USING ARGS IN DECORATOR
def result(func):
    def inner(*args,**kwargs):
        if args[0] >= 35:      # USING ARGS FOR COMPARISON
            print("PASS")
        else:
            print("FAIL")

        func(*args,**kwargs)
    return inner


def grade(func):
    def inner(*args,**kwargs):
        if args[0] > 0 and args[0] < 30:
            print("GRADE E")

        elif args[0] >= 30 and args[0] < 50:
                print("GRADE D")
        elif args[0] >= 50 and args[0] < 70:
            print("GRADE C")
        elif args[0] >= 70 and args[0] < 90:
            print("GRADE B")
        elif args[0] >= 90:
            print("GRADE A")

        func(*args,**kwargs)

    return inner


# 2 decorators
@result
@grade
def marks(total_marks):
    print("Marks obtained:", total_marks)

# HERE WE HAVE TO PASS ARGS TYPE OF ARGUEMENT
marks(95)

# marks(total_marks = 95) -> ERROR -> IT WILL SHOW TUPLE INDEX OUT OF RANGE BCOZ WE HAVE KWARGS TYPE ARGUEMENT



# ------------------------------------------------------------------------
print("-"*30)


# HERE IN 2nd EXAMPLE,WE ARE USING KWARGS ARGUEMENT
def transaction(func):
    def inner(*args,**kwargs):

        if kwargs['amount'] >= 100:     # HERE WE HAVE TO MENTION PARAMETER NAME WITH KWARGS
            print("Processing the transaction")
        else:
            print("Invalid transaction")
        func(*args,**kwargs)
    return inner




@transaction
def pay(amount):
    print("Transacting the amount:", amount)

# HERE IT IS TAKING VALUE WITH KEYWORD MEANS KWARGS TYPE OF ARGUEMENT
pay(amount=100)