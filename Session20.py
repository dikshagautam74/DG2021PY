# Assignment of brick in the wall using function

import argparse
import sys


log = {
    "i": "john",
    "j": "jack",
    "k": "applying_bricks",
    "message": "john and jack are working on the construction of wall"

}


def bricks(args):
    if args.o == "calculate":

        n = args.bricksrequired
        k = args.progress_of_bricks_in_wall


    turns_of_john = 0
    turns_of_jack = 0
    for i in range(1, n):

        if k == n:
            break


        elif k + i > n:

            i = n - k
            k += i

            print("i=", i)
            print("k in I =", k)
            print("John planted last")
            print("Wall Made")

            break



        elif k < n:
            print("i =", i)
            k += i
            print("k in I =", k)

        for j in range(1, n):

            if j == i:
                turns_of_jack = j
                # print("Turns Of Jack:", b)
                j = i * 2

                if k + j > n:

                    j = n - k
                    k += j

                    print("j=", j)
                    print("k in J =", k)
                    print("Jack planted last")
                    print("Wall Made")
                    break

                elif k == n:
                    break


                elif k < n:
                    print("j =", j)
                    k += j
                    print("k in J =", k)

        turns_of_john = i

    print("Turns Of John:", turns_of_john)
    print("Turns Of Jack:", turns_of_jack)



def write_log():
    log_to_write = "{i},{j},{k},{message}\n".format_map(log)


    with open("bricks.txt", "a") as file:
        file.write(log_to_write)
        print("Log Written...", end="")



def main():


    obj = argparse.ArgumentParser()

    obj.add_argument("--bricksrequired", type=int)
    obj.add_argument("--progress_of_bricks_in_wall", type=int)
    obj.add_argument("--o", type=str)


    args = obj.parse_args()


    sys.stdout.write(str(bricks(args)))
    sys.stdout.write(str(write_log()))


if __name__ == '__main__':
    main()


