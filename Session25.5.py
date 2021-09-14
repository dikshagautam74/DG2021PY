"""
 In this we are using SpinBox class , in this we gave the limits i.e. from how much to how much you want
 to create a window with selection from 1-10.
"""


from tkinter import *

window = Tk()
window.title("Spin Box")

spin_box = Spinbox(window, from_=1, to=10, width=10)
spin_box.pack()

window.geometry("300x300")
window.mainloop()