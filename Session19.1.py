
#  Argument Parsing

import argparse

# dictionary
log = {
    "date": "11 Aug 2021",
    "time": "11:27",
    "severity": "high",
    "message": "[DEVICE WORKING]: this is an initial log"
}

# write log dictionarty  in the file
def write_log(file_name):
    log_to_write = "{date},{time},{severity},{message}\n".format_map(log)
    with open(file_name, "a") as file:
        file.write(log_to_write)
        print("Log Written...", end="")   # end gives a new line before printing


# reads log from the file
def read_logs(file_name):
    with open(file_name, "r") as file:
        for log_in_file in file.readlines():
            print(log_in_file, end="")


def main():
    # ArgumentParser() is a class , argparse is a module from which are accessing ArgumentParser class
    # ap is an object of class ArgumentParser
    ap = argparse.ArgumentParser()

    # add_argument is a built-in function to take arguements from the user
    ap.add_argument("-o", "--operation", required=True, help="please give operation as read or write")
    ap.add_argument("-f", "--filename", required=True, help="please give filename eg logs.csv")

    # parse_args is a built-in function
    # parse_args will take the arguments you provide on the command line when you run your program and
    # interpret them according to the arguments you have added to your ArgumentParser object
    result = ap.parse_args()
    print(result, type(result))

    args = vars(result)
    print(args, type(args))

    if args['operation'] == "write":
        write_log(file_name=args['filename'])
    else:
        read_logs(file_name=args['filename'])

if __name__ == '__main__':
    main()