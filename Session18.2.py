"""
 INHERITANCE

  What is Inheritance ?
  IS-A Relationship -> Parent and Child
  Parent: John Watson
  Child: Fionna Watson
  Hence Fionna IS-A Watson :)
"""

class Parent:
    def __init__(self):
        print("Parent object constructed")
        print("self is:", self)
        print("type of self is:", type(self))
        print()

    def show(self):
        print("show of Parent")

# INHERITANCE SYNTAX
class child(Parent):
    def __init__(self):
        print("child object constructed")
        print("self is:", self)
        print("type of self is:", type(self))
        print()



def main():
    print("Details of Parent:", vars(Parent))
    print("Details of Child:", vars(child))
    print()

    # it runs only,when we have made a constructor of child class
    # but if we haven't made it,it will not run,but due to inhertance,child1 gets executeda as child is inheriting parent class

    # HERE CHILD HAS IT'S CONSTRUCTOR,SO IT WILL NOT USE PARENT CLASS CONSTRUCTOR
    child1 = child()
    print("child1 is:", child1)

    # here child has not it's show function,but due to inheritance,it takes show() of parent
    child1.show()

if __name__ == '__main__':
    main()