# RECURSION

def find_max(data, length):
    if length == 1:
        return data[0]
    else:
        result = find_max(data, length-1)
        print("result is :", result)

        if result > data[length-1]:
            return result
        else:
            print("data[length-1]:", data[length-1])

            return data[length-1]

def main():
    numbers = [10, 20, 30]
    print(numbers)
    max = find_max(numbers, len(numbers))
    print("MAX IS:", max)


if __name__ == '__main__':
    main()