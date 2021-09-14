"""
   PRIVATE
   PROTECTED
"""

class Student:
    def __init__(self, name, roll, age):
        # value of parameters are assigned in variables with self(Name, _Roll, __Age)

        self.Name = name
        self._Roll = roll   # with one underscore the variable Roll becomes "Protected"

        # here with 2 underscores the variable Age becomes "Private" i.e.
        # it can only be accessed in class only ,outside the class it will give ERROR
        self.__Age = age


    def show(self):
        print("Name:",self.Name)

        # here accessing these variables will not give error, as they are accessed inside the class
        print("Roll and Age:", self._Roll, "|\t", self.__Age)



def main():
    student = Student("john",12,5)

    # print(vars(student))
    student.show()
    print(student.Name)
    print(student._Roll)   # it will give warning
    # print(student.__Age)    it will give ERROR

    # NAME MANGLING -> __Age will be renamed to _Student__Age
    # now it will not give error
    print(student._Student__Age)


if __name__ == '__main__':
    main()