from tkinter import *
from tkinter import filedialog

def on_click():

    # it will open the file manager window,ask to open a file
    file_path = filedialog.askopenfilename()
    print(file_path)


window = Tk()
window.title("Picking Files")

# Menu() is builtin class
menu = Menu()

# item means like File,edit,view,navigate written above
# item = Menu()
item = Menu(menu)

# add_command -> adds features in that menu
item.add_command(label="New")
item.add_command(label="Save")

# add_separator will give a line
item.add_separator()

item.add_command(label="Exit")

# add_cascade -> it's like a category,that what name you want to give to item, parameter menu -> item that are added(command) are assigned to menu
menu.add_cascade(label="FILE", menu=item)


btn_select_file= Button(window, text="SELECT FILE", command=on_click)
btn_select_file.pack()

# configure means put all the items altogether in a menu called 'FILE'
window.config(menu=menu)

window.geometry("300x300")

window.mainloop()