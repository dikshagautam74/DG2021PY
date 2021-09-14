# DUCK TYPING  -> it means if a thing do quack quack,then it means it's a duck.
# in the below eg. class Cab,OLAMini,OLASedan has same function i.e. book_cab means they are behaving same
# but the class truck has not book_cab function,it is behaving different, so it do not duck typing
# in short,class Cab,OLAMini,OLASedan are doing quack quack,but truck doesn't.

class Cab:
    def book_cab(self):
        print("Cab Booked")

class OLAmini():
    def book_cab(self):
        print("Ola Mini cab Booked")

class OLAsedan():
    def book_cab(self):
        print("Ola Sedan cab Booked")


class Truck():
    def book_truck(self):
        print("truck booked")

# this function is used to test duck typing, as when objects passed as reference to obj one by one,
# book_cab function gets called, and if any obj has not that function it will error.
def testing_duck_typing(obj):
    obj.book_cab()


cab = Cab()
testing_duck_typing(cab)

mini = OLAmini()
testing_duck_typing(mini)

sedan = OLAsedan()
testing_duck_typing(sedan)


truck = Truck()
testing_duck_typing(truck)   # ERROR -> as truck has no book_cab function



"""

  DUCK TYPING WITH INHERITANCE
  
  #now here OLAMini and OLASedan has access to class Cab's book_cab function due to inheritance
  #but truck has not access to that.
  

class Cab:

    def book_cab(self, source, destination):
        print("Cab Booked from {} to {}".format(source, destination))


class OLAMini(Cab):
    pass


class OLASedan(Cab):
    pass

#- here truck is not inheriting Cab,so it will not get access to book_cab function
class Truck:

    def book_truck(self, source, destination, load=100):
        print("Truck Booked from {} to {} with load of {} kgs".format(source, destination, load))


def duck_testing(ref):
    ref.book_cab("Home", "Work")

cab = Cab()
duck_testing(cab)

cab = OLAMini()
duck_testing(cab)

cab = OLASedan()
duck_testing(cab)

cab = Truck()
duck_testing(cab) 
 
"""