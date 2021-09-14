#  TIME COMPLEXITY -> O(n)
for i in range(1,10):
    print(i)


#  TIME COMPLEXITY -> O(n*n)
for i in range(1,9):
    for j in range(1,6):
        print(j)


#  TIME COMPLEXITY -> O(n*n*n)
for i in range(1,9):
    for j in range(1,6):
        for k in range(1,5):
            print(k)

# Total time complexity -> O(n) + O(n*n) + O(n*n*n) = O(n*n*n)