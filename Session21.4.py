# import Session21C
import Session21C as S    # S is the alias name for Session21C means writing Session21C in short as S
# in place of Session21C now u can write only S , it will work same.

print()

print("This is Session21.4")
print("__name__ for Session21.4 is:", __name__)

print()

# u can have access to Session21C's attribute 'name' with the help of Session21C.Can't directly print it.
# print("Imported:", Session21C.name)
print("Imported:", S.name)


print()

# accessing Session21C function 'show' outside the class
# Session21C.show()
S.show()

# access to Session21C class's inside function, ref is a kind of object of training class.
# ref = Session21C.training()
# ref.fun()
# print(ref)

ref1 = S.training()

ref1.fun()
print(ref1)
