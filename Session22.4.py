"""
 Assignment
"""

ipl = {
    "delhi capitals":{
        "M": 8,
        "W": 6,
        "L": 2,
        "T": 0,
        "N/R": 0,
        "PT": 12
    },
    "chennai super kings ":{
        "M": 7,
        "W": 5,
        "L": 2,
        "T": 0,
        "N/R": 0,
        "PT": 10
    },
    "royal challangers bangalore":{
        "M": 7,
        "W": 5,
        "L": 2,
        "T": 0,
        "N/R": 0,
        "PT": 10
    },
    "mumbai indians":{
        "M": 7,
        "W": 4,
        "L": 3,
        "T": 0,
        "N/R": 0,
        "PT": 8
    },
    "rajashtan royals":{
        "M": 7,
        "W": 3,
        "L": 4,
        "T": 0,
        "N/R": 0,
        "PT": 6
    },
    "punjab kings":{
        "M": 8,
        "W": 3,
        "L": 5,
        "T": 0,
        "N/R": 0,
        "PT": 6
    },
    "kolkata knight riders":{
        "M": 7,
        "W": 2,
        "L": 5,
        "T": 0,
        "N/R": 0,
        "PT": 4
    },
    "sunrisers hyderabad":{
        "M": 7,
        "W": 1,
        "L": 6,
        "T": 0,
        "N/R": 0,
        "PT": 2
    }

}



def write():

    with open("match.csv", "w") as file:

        for data in ipl:
            print(data, ipl[data], file=file)


    # file.write()

write()
