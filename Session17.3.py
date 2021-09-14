# it will open the file Session17.2 and we are going to read this
# "r" -> we are going to read this
file = open("Session17.2.py","r")

# applying read operation and passed its reference to contents
# contents = file.read()

# contents = file.read(10)

# # printing the contents of file Session17.2
# print(contents)

# contents = file.read(10)
# print(contents)

# print(type(contents))

# ---------------------------------------------


# seek ->  move/set the cursor to 10th character means it defines from where the data has to be read
# file.seek(10)

# # it will tell you the cursor position
# cursor_position = file.tell()
# print("cursor position :", cursor_position)

# # it will print the contents from character 10
# contents = file.read()
# print(contents)
#-----------------------------------------------


# now without setting the cursor position,it will print u the cursor position as '0'.
# cursor_position = file.tell()
# print("cursor position :", cursor_position)

# # now the file is readed
# contents = file.read()

# # after the file is read,the cursor will move to the last character,so it will tell u the cursor position as
# # last character , Basically  u come to know how many characters are there in ur file
# cursor_position = file.tell()
# print("cursor position :", cursor_position)
#---------------------------------------------------


# contents = file.read()
# # it will not print anything as the file is already read above,so now there is nothing to read in file
# print("contents:", contents)
#----------------------------------------------------



# it will read the lines in a file
lines = file.readlines()
# it will print u the lines which are returned in a list
print("lines:", lines)
print("length:", len(lines))    # total no. of lines
print("type:", type(lines))

for_loops = 0
for line in lines:
    print(line)   # print u the line one by one
    print()

    if "for" in line:
        for_loops += 1

print("total for loops:", for_loops)


# Project #1
# Source Code Generator Like Siri/Alexa
# i.e. create a BOT

# Project #2
# Source Code Analysis i.e. Profiling -> means a program which calculate the time complexity and how many
# nested for loops are there
# Tell/Compute the time complexity of Program

