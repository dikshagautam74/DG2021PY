"""
  @classmethod DECORATOR ->  A BUILT-IN DECORATOR
  FOR THIS,WE DON'T HAVE TO MAKE ANY OBJECT
"""

class MovieTicket:

    # no. of seats in different rows in a cinema hall
    cinema_hall = {
        "A":10,
        "B": 8,
        "C": 15,
        "D": 12,
        "E": 10,
        "F": 10
    }

     # it will calculate the total seats in a cinema hall by their values
    total_seats = sum(cinema_hall.values())

    ticket_number = 1

    def __init__(self, movie, date, time):

        # can't access property of class without class name
        # self.ticket_number = ticket_number

        # don't have to give ticket_number as a parameter
        self.ticket_number = MovieTicket.ticket_number
        self.seat = MovieTicket.cinema_hall["A"]      # it has taken A from cinema hall dictionary

        self.movie = movie
        self.date = date
        self.time = time

        # this is the logic or it is a same scene like in a cinema hall
        # MovieTicket.cinema_hall["A"] -= 1
        # MovieTicket.total_seats -= 1
        # MovieTicket.ticket_number += 1

    def show(self):
        pass
    # ----------------------------------------


    # builtin decorator
    # it will take reference of class as input
    @classmethod
    def create_tickets_from_file(cls):
        print("cls is:", cls)
        print("vars(cls):", vars(cls))

        # print(cls.cinema_hall)

        file = open("tickets.csv", "r")
        lines = file.readlines()

        # CREATING AN EMPTY LIST TO APPEND THE OBJECTS
        tickets = []

        for line in lines:
            data = line.split(",")
            print("data:", data)

            # it's like an object of class MovieTicket ,cls = MovieTicket
            ref = cls(
                movie=data[0],
                date=data[1],
                time=data[2]
            )

            # ref = MovieTicket(
            # movie=data[0],
            # date=data[1],
            # time=data[2]
            # )

            # appending 2 more attributes in object
            ref.ticket_number = cls.ticket_number
            ref.seat = cls.cinema_hall["A"]

            cls.cinema_hall["A"] -= 1
            cls.total_seats -= 1
            cls.ticket_number += 1

            # APPENDING THE OBJECTS ONE BY ONE
            tickets.append(ref)

        return tickets




def main():
    # ticket1 = MovieTicket(movie="uri",date="13th Aug,2021",time="14:00")
    # ticket2 = MovieTicket(movie="hey baby",date="14th Aug,2021",time="15:00")
    #
    #
    # print(vars(ticket1))
    # print(vars(ticket2))
    # print(vars(MovieTicket))

    # print()

    # u can access this function with reference variable also and with the class name also
    # ticket1.create_tickets_from_file()

    tickets = MovieTicket.create_tickets_from_file()

    print("TICKET OBJECTS FROM FILE")
    for ticket in tickets:
        print(vars(ticket))


if __name__ == '__main__':
    main()