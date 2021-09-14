"""
  Meta programming
  DECORATORS
"""

def header(func): #Step 2. control will come here

    def menu_bar():                                            # Step 6. it will execute now
        print("-"*30)                                          # Step 7.  it got printed
        print("Before decorating ")                            # Step 8.  it got printed
        print("-"*30)                                          # Step 9.  it got printed

        func()   # Step 10.  func() is executed , as we have passed reference of home to func variable, now it become a function
                 # Step 13. now control will move from here as it has completed his execution

        print("After decorating")                             # Step 14. it got printed

    # this is returning to header()
    return menu_bar                                          # Step 3. returning menu_bar to header()


# @header
# this is the function we want to decorate without modifying it.
def home():       # Step 11. as func() has reference of home and it is executed,so now home will get executed
    print("Welcome to My App")                                # Step 12. it will printed

# result variable is used here to store menu_bar function
result= header(func=home)                        #Step 1. control will come here,it is calling header()
                              #Step 4. menu_bar() will assigned to result and result becomes a function

result()    #/ menu_bar() -> it works like this     Step 5. menu_bar will be called now

# home()