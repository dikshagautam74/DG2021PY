# SET

followers = {"robin", "era", "jack", "joe"}
print("followers:", followers)

# LIST
list_numbers = list(range(10,101,10))
print("numbers in list:", list_numbers)

list_numbers.append(40)
list_numbers.append(70)
print("list_numbers after appending :", list_numbers)

# SET
# here the list is converted into set , in the output the elements will be in unordered way
set_numbers = set(list_numbers)
print("number in set:", set_numbers)

# appending doesn't work in set. TO add an element we can use ADD().
# adding same element in set does not affect the set,as it has only unique elements
# as 40 is already in the set,so it is not added again.

set_numbers.add(40)
print("set_numbers after adding :", set_numbers)

#set_numbers.update({1,2,3,4})   -> adding another set in set_numbers
#set_numbers.update((6,12,34,56), {1,2,3,4})  -> adding a tuple and another set in set_numbers
set_numbers.update([34,778,56], {1,2,3,4})    #-> adding a list and another set in set_numbers

print("set_numbers after updating:", set_numbers)

# pop() will remove the topmost element from set_numbers as in stack
set_numbers.pop()
print("set_numbers after popping element:", set_numbers)

print("length of set_numbers:", len(set_numbers))
print("maximum of set_numbers:", max(set_numbers))
print("minimum of set_numbers:", min(set_numbers))

# removing an element from set
set_numbers.remove(34)

# removing an element which is not in the set,will give error with remove()
#set_numbers.remove(35)

# removing an element which is not in the set,will not give error with discard()
set_numbers.discard(35)
print(set_numbers)

print()

brand1 = {"nike", "h&m", "puma","adidas", "puma","zara"}
brand2 = {"nike", "h&m", "puma"}

print("brand 1 :", brand1)
print("brand 2 :", brand2)

brand3 = brand1.union(brand2)
print("union of brand 1 and brand 2:", brand3)

brand3 = brand1.intersection(brand2)
print("intersection of brand 1 and brand 2:", brand3)

print("Is brand 2 of subset of brand 1 ?:", brand2.issubset(brand1))
print("Is brand 1 of superset of brand 2 ? :", brand1.issuperset(brand2))

print()

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#union of sets
# with function
C = A.union(B)
# with operator
#C = A | B
print("union of A & B :",C)

# intersection of sets
# with function
C = A.intersection(B)
# with operator
#C = A & B
print("intersection of A & B :",C)

# symmetric difference of sets
# with function
C = A.symmetric_difference(B)
# with operator(EXOR)
#C = A ^ B
print("symmetric difference of A & B :",C)

# DIFFERENCE OPERATION WITH DIFFERENCE() FUNCTION
C = A.difference(B)
# DIFFERENCE OPERATION WITH OPERATOR
C = A - B
print("difference of A & B :", C)

# frozen set
data = {1, 2, 3, 4, 5, 1, 2}
print("data is :", data)

f_set = frozenset(data)
print("frozen set is :", f_set, type(f_set))

# in frozen set if u want to add,it will not add as by name it is frozen
#f_set.add(7)
#print(f_set)

