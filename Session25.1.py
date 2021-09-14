from tkinter import *
from tkinter.ttk import *   # ttk is imported to use ComboBox,BooleanVar

def on_click():
    print("Button Clicked")
    print("City selected:", combo_box.get())         # get() -> returns the text which we have seelcted from combo_box values
    print(state.get())

window = Tk()
window.title("HomePage")

lbl_title = Label(window, text="Welcome to the Home Page")
# lbl_title.pack()
lbl_title.grid(column=0, row=0)   # grid sets the statement according to row and column.

btn_submit = Button(window, text="SUBMIT", command=on_click)
btn_submit.grid(column=0, row=1)

# it takes a list of values from which we can select
combo_box = Combobox(window)
combo_box['values'] = ("Select City", "Ludhiana", "Chandigarh", "Delhi", "Bangalore")
combo_box.current(0)     # it sets 'select city' in the position from which we come to know that we have to select city
combo_box.grid(column=0, row=2)

# booleanVar takes 2 values 'True' and 'False'
# if we tick the condition , it will return us 'true' in get() , if we don't tick,it returns false
state = BooleanVar()
# var=state -> variable state of type BooleanVar whose value is either True or False.
check_button = Checkbutton(window, text="I agree to the terms and conditions", var=state)
check_button.grid(column=0, row=3)


# it sets the window size of 400x400,we can give any size
window.geometry('400x400')
window.mainloop()
