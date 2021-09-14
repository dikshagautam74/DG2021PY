"""
 Argument parsing
  1.sys
  2.getopt -> explore urself
  3.argparse

"""
# system module
import sys


def write_in_file(data="Hello"):
    # 'with' is written bcoz if we don't have a file created,write() will create the file,but read will give error
    with open("data.txt","a") as file:
        file.write(data)

def read_from_file():
    # 'with' is written bcoz if we don't have a file created,write() will create the file,but read will give error
    with open("data.txt","r") as file:
        for line in file.readlines():
            print(line)

def main():
    print("number of arguments:", len(sys.argv))
    print("Arguments:", sys.argv)

    # when u give argument "write" at 1st index in terminal,your file gets created
    if sys.argv[1] == "write":
        write_in_file()
    elif sys.argv[1] == "read":
        read_from_file()

# this u have to run in terminal
# write 'python Session19.py hi hello'
# after python it will take every word as an argument

if __name__ == '__main__':
    main()