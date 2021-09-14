# CHAINING DECORATORS


def result(func):
    def inner(total_marks):
        if total_marks >= 35:
            print("PASS")
        else:
            print("FAIL")

        func(total_marks)
    return inner


def grade(func):
    def inner(total_marks):
        if total_marks > 0 and total_marks < 30:
            print("GRADE E")

        elif total_marks >= 30 and total_marks < 50:
                print("GRADE D")
        elif total_marks >= 50 and total_marks < 70:
            print("GRADE C")
        elif total_marks >= 70 and total_marks < 90:
            print("GRADE B")
        elif total_marks >= 90:
            print("GRADE A")

        func(total_marks)

    return inner


# 2 decorators
@result
@grade
def marks(total_marks):
    print("Marks obtained:" ,total_marks)

marks(95)



# final = result(marks)
# final(95)
#
# final = grade(marks)
# final(95)
