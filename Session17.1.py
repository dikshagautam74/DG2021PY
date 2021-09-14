cpp_source_code = """
# include<iostream>
using namespace std;
int main(){
  cout<<"Hello World";
  return 0;
}
"""
dart_source_code = """
void main(){
  print("Hello World");  
}
"""
java_source_code = """class App{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
"""

python_source_code = """
print("Hello World")
"""



"""
ONE WAY TO SAVE THE FILE 

print("We will generate a hello world program")
print("which source code would you like to generate")
choice = input("Enter programming language:")


# default values
file_name = ""
data = None

if choice == "cpp":
    file_name="hello.cpp"  # file will be saved by this name
    
    # when you open the file in downloads , there should be some data, and it will be the code written here 
    data = cpp_source_code
    
elif choice == "java":
    file_name="hello.java"
    data = java_source_code
    
elif choice == "dart":
    file_name="hello.dart"
    data = dart_source_code
    
elif choice == "python":
    file_name="hello.py"
    data = python_source_code
    
else:
    print("Sorry! I do not support generating source code for:",choice)
    
# save the file in downloads instead of saving here     
if len(file_name) != 0:   # if file_name is not empty
    # our file will be created and gets stored in downloads using this url
    file = open("/Users/hp/Downloads/{}".format(file_name), "w")
    file.write(data)
    print("Source Code Saved :)")
    print("Please check your downloads directory")
"""

#---------------------------------------------------------------------
# ANOTHER WAY OF SAVING FILE


# you can create a dictionary rather than writing variables
file_contents = {
    "file_name": "",
    "data": ""
}

print("We will generate a hello world program")
print("which source code would you like to generate")
choice = input("Enter programming language:")

if "cpp" in choice:
    file_contents['file_name'] = "hello.cpp"
    file_contents['data'] = cpp_source_code
elif "dart" in choice:
    file_contents['file_name'] = "hello.dart"
    file_contents['data'] = dart_source_code
elif "java" in choice:
    file_contents['file_name'] = "hello.java"
    file_contents['data'] = java_source_code
elif "python" in choice:
    file_contents['file_name'] = "hello.py"
    file_contents['data'] = python_source_code
else:
    print("Sorry! I do not support generating source code for:",choice)

# file_name is in file_contents,so we have to write like this
if len(file_contents['file_name']) != 0:    # if file_name is not empty

    # our file will be created and gets stored in downloads using this url
    file = open("/Users/hp/Downloads/{}".format(file_contents['file_name']), "w")

    file.write(file_contents['data'])   # it will write the data in file and our code will run also.
    print("Source Code Saved :)")
    print("Please Check your Downloads Directory")






