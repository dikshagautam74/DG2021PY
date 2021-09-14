"""
Another program for reference copy with multi value container
"""

numbers = [10, 20, 30, 40, 50]

# Reference copy -> Multi value container
my_numbers = numbers

print("numbers is :", numbers, "and hash code is :", hex(id(numbers)))
print("my numbers is :", my_numbers, "and hash code is :", hex(id(my_numbers)))

print("DATA IN NUMBERS BEFORE")
for num1 in numbers:
    print(num1, hex(id(num1)))

print("DATA IN MY NUMBERS BEFORE")
for num2 in my_numbers:
    print(num2, hex(id(num2)))

print()

for i in range(0, len(numbers)):
    numbers[i] += 5          # here value of my_numbers will also get changed

    print("numbers now is :", numbers, "and hash code is :", hex(id(numbers)))
    print("my numbers now is :", my_numbers, "and hash code is :", hex(id(my_numbers)))

    print()



print("DATA IN NUMBERS AFTER")
for num3 in numbers:
    print(num3, hex(id(num3)))


print("\n DATA IN MY NUMBERS AFTER")
for num4 in my_numbers:
    print(num4, hex(id(num4)))



