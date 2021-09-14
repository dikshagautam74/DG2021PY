"""
 scrolled text module
 u can write any amount of text you wish to write
 u can write notes in this.
"""

from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Scrolled Text")

# ScrolledTest is a builtin class.
scroll_text = scrolledtext.ScrolledText(window, width=240, height=100)
scroll_text.grid(column=0, row=0)



window.geometry("300x300")
window.mainloop()