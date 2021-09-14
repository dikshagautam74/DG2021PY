import os

print(os.name)
# print(os.uname())  not in windows
print(os.getlogin())
print("current working directory:", os.getcwd())
print(os.getppid())

path_to_directory = "C:/Users/hp/OneDrive/Pictures/Screenshots"
path_to_file = "C:/Users/hp/Downloads/77629.pdf"

# check whether path inputed of directory and file is same as in our system
print(os.path.isdir(path_to_directory))
print(os.path.isfile(path_to_file))

files = os.walk(path_to_directory)
files = list(files)
for file in files:
    print("file:", file)
    print("length of file:", len(file))

for data in files[0]:
    print("data:", data, "length:", len(data))



print("Directories:", len(files[0][1]))
print("files:", len(files[0][2]))