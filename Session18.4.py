"""
 RUNTIME POLYMORPHISM

 THERE IS NO COMPILE TIME POLYMORPHISM IN PYTHON
"""

class payment:

    def pay(self, amount):
        print("Please Pay:", amount)


# payment class inherited
class netBanking(payment):

    def input_username_password(self):

        print("Enter Username and Password")


    # re-defining
    def pay(self, amount):
        netBanking.input_username_password(self)
        # self.input_username_password()   -> another way to access the above function
        print("Please Pay:", amount)


class upi(payment):

    def input_upi_id(self):
        print("Enter Upi Id")

    def pay(self, amount):
        upi.input_upi_id(self)
        print("Please Pay:", amount)


# FACTORY DESIGN PATTERN
class paymentMethod:
    # DECORATOR
    @classmethod
    def get_method(cls,type):
        ref = None

        if "netBanking" in type:
            ref = netBanking()
        elif "upi" in type:
            ref = upi()
        else:
            print("Invalid option")

        return ref
def main():


   """runtime polymorphism

    OBJECT CREATION OF DIFFERENT CLASSES
    ref = payment()
    ref.pay(1000)

    ref = upi()
    ref.pay(1000)

    ref = netBanking()
    ref.pay(1000)"""


choice = input("How would you like to pay:")
Payment = paymentMethod.get_method(type=choice)
if Payment is not None:
    Payment.pay(amount=1000)



if __name__ == '__main__':
    main()