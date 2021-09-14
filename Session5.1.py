base_fare = 50
type_of_cab = input("Enter type of cab")

cabs = { "mini":50 ,"sedan":100 ,"bike":30}

#this is 3rd method to book a cab in only 1 line
#here get() is used if we want to book any other unavilable cab,it gives a default value(i.e.-base_fare)
# and get us the cab which is available(i.e.type_of_cab)
print(type_of_cab,"booked","Please Pay: \u20b9", base_fare+cabs.get(type_of_cab,-base_fare))

"""
this is a 2nd method to book a cab
if type_of_cab in cabs:
    print(type_of_cab,"booked.Please Pay:",base_fare+cabs[type_of_cab])
"""


"""
this is a 1st big method to book a cab
#Ladder If/else
if type_of_cab == "mini":
    base_fare += 50
    print("Mini car booked . Please Pay:",base_fare)
elif type_of_cab == "sedan":
        base_fare += 100
        print("Sedan booked . Please Pay:", base_fare)
elif type_of_cab == "bike":
            base_fare += 30
            print("Bike booked . Please Pay:", base_fare)
else:
    print("Please select the cab to proceed")
"""