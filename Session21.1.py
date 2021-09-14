"""
  HOW TO CRASH THE PROGRAM EXPLICITLY

"""

def main():
    print("APP STARTED")

    # raising INDEXERROR by ourselves , it's not due to the wrong program
    raise IndexError("Crashing the app as Developer")

    print("APP FINISHED")


if __name__ == '__main__':
    main()