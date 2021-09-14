"""
    GUI | Graphical User Interfaces
    >> figma (Design Your GUI First)

    tkinter
    PyQT -> Explore
"""
# package
from tkinter import *
from Session24 import DB



def on_click():
    print("Button Clicked")

    customer = {
        "name": entry_name.get(),    # get() -> u will get the name of the customer
        "phone": entry_phone.get(),
        "email": entry_email.get()
    }

    # object made of DB class;made in Session24
    my_db = DB()
    sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', 0.0, '', '')"\
        .format_map(customer)
    my_db.execute_sql_write_operation(sql)

    print(customer)

def main():

    global entry_name
    global entry_phone
    global entry_email

    # TK() is an interface
    window = Tk()

    lbl_title = Label(window, text="CUSTOMER MANAGEMENT SYSTEM")
    lbl_title.pack()

    lbl_phone = Label(window, text="Enter Customer Name:")
    lbl_phone.pack()

    entry_name = Entry(window)
    entry_name.pack()

    lbl_phone = Label(window, text="Enter Customer Phone:")
    lbl_phone.pack()

    # Entry means u can give an entry to the asked question,like it makes an empty box for u to do entry.
    entry_phone = Entry(window)
    entry_phone.pack()

    lbl_email = Label(window, text="Enter Customer Email:")
    lbl_email.pack()

    entry_email = Entry(window)
    entry_email.pack()

    btn_submit = Button(window, text="Add Customer", command=on_click)
    btn_submit.pack()

    window.mainloop()

if __name__ == '__main__':
    main()