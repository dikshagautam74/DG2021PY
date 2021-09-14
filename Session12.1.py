# IMPORTING SESSION 12 IN SESSION 12.1 WILL PRINT US THE THINGS IN SESSION 12.1 MADE IN SESSION 12
import Session12
# when we import session 12 __name__ will print us the name of the imported session i.e session 12

print()

print("This is Session 12.1")
print("Name of Session 12.1 is :", __name__)   # here it will print __main__ only not Session 12.1

# here we can't directly call the Session 12's fun()
# fun()
# we can call fun() by accessing it with Session 12
Session12.fun()