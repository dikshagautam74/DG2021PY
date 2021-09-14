from tkinter import *
from tkinter.ttk import *

def on_click():
    print("Button clicked")
    print(var.get())

window = Tk()
window.title("Radio Buttons")

lbl_gender = Label(window, text="Select Gender")

# IntVar is a builtin function,means var will be of integer type
var = IntVar()

# IntVar is used bcoz we have to select one gender only,if don't use it will select all genders
rb_female = Radiobutton(window, text="Female", value=1, variable=var)  # female will take 1 from var
rb_male = Radiobutton(window, text="Male", value=2, variable=var)
rb_not_to_say = Radiobutton(window, text="Not To Say", value=3, variable=var)

btn = Button(window, text="SUBMIT", command=on_click)


lbl_gender.grid(column=0, row=0)
rb_female.grid(column=0, row=1)
rb_male.grid(column=1, row=1)
rb_not_to_say.grid(column=2, row=1)
btn.grid(column=0, row=3)



window.mainloop()
