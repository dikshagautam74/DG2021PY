"""
  INHERITANCE
"""

class flightBooking:
    def __init__(self, from_location, to_location, departure_date, travellers, travel_class):

        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers
        self.travel_class = travel_class


    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.from_location, "->", self.to_location)
        print(self.departure_date)
        print(self.travellers, self.travel_class)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



class roundTripFlightBooking(flightBooking):
    def __init__(self,from_location, to_location, departure_date, travellers, travel_class,return_date):
        flightBooking.__init__(self, from_location, to_location, departure_date, travellers, travel_class)
        self.return_date = return_date


    def show(self):
        # accessing parent class's show method -> by this we don't have to write this code again
        flightBooking.show(self)
        print(self.return_date)



def main():
    one_way_booking = flightBooking(from_location="Delhi", to_location="Bangalore", departure_date="12th Aug 2021",travellers=2, travel_class="economy")
    print(vars(one_way_booking))

    print()

    two_way_booking = roundTripFlightBooking(from_location="Delhi", to_location="Bangalore", departure_date="12th Aug 2021", travellers=2, travel_class="economy", return_date="20th Aug 2021")
    print(vars(two_way_booking))

    two_way_booking.show()



if __name__ == '__main__':
    main()