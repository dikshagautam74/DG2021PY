import pymongo
import ssl # if you get SSL Certificate Error

class Student:

    def __init__(self, input_flag=False, roll=0, name="NA", email="NA", age=0):
        if input_flag:
            self.roll = int(input("Enter Roll Number: "))
            self.name = input("Enter Your Name: ")
            self.email = input("Enter Your Email: ")
            self.age = int(input("Enter Age: "))
        else:
            self.roll = roll
            self.name = name
            self.email = email
            self.age = age

    def __str__(self):
        return "{roll}, {name}, {email}, {age}".format_map(vars(self))


class DB:

    def __init__(self):
        db_config = {
            "username": "diksha",
            "password": "dikshag",
            "db_name": "gw2021py1"
        }
        db_uri = "mongodb+srv://{username}:{password}@cluster0.1x52c.mongodb.net/{db_name}?retryWrites=true&w=majority".format_map(
            db_config)
        # self.db = client.test
        client = pymongo.MongoClient(db_uri)
        client = pymongo.MongoClient(db_uri, ssl_cert_reqs=ssl.CERT_NONE) # if you get SSL Certificate Error
        self.db = client.test

        print("DB Connection Created :)")

        # self.db = client.gw2021py1
        self.db = client['gw2021py1'] # get the reference of our database
        collections = self.db.list_collection_names()     # gives a list of collections u have in mongodb database gw2021py1
        print("Collections:", collections)

        # Select the Collection in which u want to insert
        self.collection = self.db['students']


    # inserting documents of student1 and student2 in mongodb
    def insert(self, document):

        self.collection.insert_one(document)
        print("Document Inserted")


def main():
    student1 = Student(input_flag=True)
    student2 = Student(input_flag=False, roll=2, name="Fionna", email="fionna@example.com", age=20)

    print(student1)
    print(student2)

    my_db = DB()
    my_db.insert(vars(student1))
    my_db.insert(vars(student2))


if __name__ == '__main__':
    main()