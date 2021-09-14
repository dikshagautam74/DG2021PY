import threading
import time
lock = threading.Lock()   # lock will lock the thread until one object complete it's execution



class MovieTicket:

    def __init__(self, name, time, row, seat):
        self.name = name
        self.time = time
        self.time = time
        self.row = row
        self.seat = seat
        self.isbooked = False


    def book_ticket(self):
        if self.isbooked:
            print("Sorry {}! Ticket is Already Booked".format(self.email))
        else:
            self.isbooked = True
            print("~"*20)
            print("Ticket booked for {}".format(self.email))
            print("Ticket:{name},{time},{row},{seat}".format_map(vars(self)))
            print("~"*20)



    def pay(self, email):
        self.email = email
        if self.isbooked:
            # print("Sorry {} Ticket is already booked")
            return

        else:
            print("[PAY] Dear {},please pay \u20b9 150".format(self.email))
            time.sleep(2)
            print("Thankyou{},Transaction finished".format(self.email))

class BookMovieTicket(threading.Thread):
    def select_seat(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        self.ticket.pay(email=self.email)
        self.ticket.book_ticket()

        lock.release()    # when one object finished it's execution,it will release the lock



def main():
    print("App started")

    row_A_tickets = [
        MovieTicket(name="Avengers", time="12:30", row="A", seat=1),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=2),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=3),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=4),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=5),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=6),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=7),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=8),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=9),
        MovieTicket(name="Avengers", time="12:30", row="A", seat=10)
    ]

    booking1 = BookMovieTicket()
    booking2 = BookMovieTicket()

    booking1.select_seat(ticket=row_A_tickets[1], email="john@example.com")
    booking2.select_seat(ticket=row_A_tickets[1], email="fionna@example.com")

    booking1.start()
    booking2.start()

    # time.sleep(1)    takes 1 second break

    print("App finished")



if __name__ == '__main__':
    main()