"""
 MONKEY PATCHING

"""

class theme:
    def show_theme(self):
        print("Show Theme")


def show_customized_theme():
    print("Customized Theme")

# object created
theme1 = theme()

# Monkey patching -> passing the reference of outside function to the function inside the class
theme1.show_theme = show_customized_theme
# calling show_theme function will give the statements of customized theme
theme1.show_theme()

# another object created
theme2 = theme()
# here we simply called show_theme function,it will print the statements of show_theme only as we don't
# have passed reference of customized theme to object2 i.e. theme2
# it will print the statement written in show_theme.
theme2.show_theme()
