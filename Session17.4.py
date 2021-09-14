from Session17 import Student

file = open("new_file", "r")
lines = file.readlines()

# creating a empty list of students
students = []

for line in lines:
    print(line, type(line))

    print()

    # here split() is used,so that the line taken from the data in new_file should be separated on the basis of comma
    # for eg. this is the first line in new_file "john,1,10,5,+91 99999 11111,male"
    # so the data will be picked on the basis of indexing
    # if we don't split the data on the basis of comma(,) , it will consider this whole line as a single string
    # it will take name as 'j';roll as 'o';age:'h';standard:'n';phone:',';gender:'1'
    # and if we use split(),it will consider 'john' as 1st index, '1' as 2nd and so on
    # other way it is taking 'j' as 1st index
    data = line.split(",")

    # making an object here which will read the data from the file
    student = Student(
        name=data[0],
        roll=data[1],
        age=data[2],
        standard=data[3],
        phone=data[4],
        gender=data[5]
    )

    # it will append the data in a students[] ,using a student object it will append the data line by line
    students.append(student)

# it will print the list objects and their hashcode
print("list of students:", students)

print()

# it will print all the student object details
for student in students:
    print(vars(student))