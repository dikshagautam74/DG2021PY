"""
 Frames -> means creating 3D border with different types of borders
 make Frames, add Frames in a Window
"""

from tkinter import *

window = Tk()
window.title("Frames")

# creating widgets of frame
# relief means type of border u want for ur frame  -> raised,flat,sunken,groove
first_frame = Frame(borderwidth=4, bg="red", relief="raised")
second_frame = Frame(borderwidth=4, bg="green", relief="flat")

# lbl1 is packed inside first_name
lbl1 = Label(master=first_frame, text="This is First Frame")
lbl1.pack()

# lbl2 is packed inside second_name
lbl2 = Label(master=second_frame, text="This is Second Frame")
lbl2.pack()

# now packing the frames in our window
#  side -> on which side ur frame should be packed/named.
first_frame.pack(side=LEFT)
second_frame.pack(side=RIGHT)

window.mainloop()