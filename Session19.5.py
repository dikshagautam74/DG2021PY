"""
    EXCEPTION HANDLING

    Compile Time Error
        python files can be compiled i.e. from .py to .pyc
        built in module -> py_compile to compile python file
        if a>b: eg: we missed the colon - > may be compile time error


    Run Time Error
        when we execute python files directly
        Whenever it occurs, nothing beyond that line will be executed

        This is a CRASH in Program
        App terminates abnormally
        TO OVERCOME THIS PROBLEM WE USE 'Robust Programming'

"""

def main():

    print("WAELCOME TO CASHBACK LUCKY DRAW")
    print("~"*30)
    print("APP STARTED")


    cashbacks = [10, 20, 23, 45, 100, 56, 21, 63, 11, 77]
    additional_cashback = 0




    # write erroronius statement inside try and except
    # if we get an error,try block will pass the control to except and statement inside except gets executed
    try:
        # here if the user enter 'nine' instead of '9', u will get ValueError,so for this one more except is used
        number = int(input("Enter your lucky number(0-9):"))

        # IF WE ADD A NUMBER WHOSE INDEX IS NOT IN RANGE, IT WILL GIVE ERROR,SO TO OVERCOME WE USE EXCEPTION HANDLING
        print("You Won \u20b9", cashbacks[number])

        additional_cashback = 0.10*cashbacks[number]
        print("Additional cashback won \u20b9:", additional_cashback)



    # write except like this also,write error name u are getting before applying try i.e. IndexError
    # except IndexError as error:
    #     print("Something Went Wrong")
    #     print("Error is:", error)     # it will print the error statement

    # ------------

    # # here u are getting 'ValueError' which taking input
    # except ValueError as error:
    #     print("Something Went Wrong")
    #     print("Error is:", error)



    # instead of using these 2 except statements,write this except statement which will handle all the errors
    # we don't have to remember all the error names
    except Exception as e:
        print("Something Went Wrong")
        print("Error is:", e)

    # simple except statement which will handle the error, but not give the error name
    # except:
    #     print("Something Went Wrong")


    # exception comes or not, 'finally' will execute
    finally:
        print("Finally Executed")


    print("APP FINISHED")



if __name__ == '__main__':
    main()