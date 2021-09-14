"""
 sql with OOPS

 Here we are seeing the corona case,that when we go somewhere our temperature is checked,name,email,phone
 and other details are taken. So it's a small program for that.

 we are using classes ,objects and some functions.

 Here the Class Customer carries the customer details as when we make object of this class,it's constructor
 gets executed.
 Class DB carries the functions to execute the operations of database sql.
"""
import mysql.connector as db


class Customer:
    def __init__(self):
        self.name = input("Enter Name")
        self.phone = input("Enter phone")
        self.email = input("Enter email")
        self.temperature = float(input("Enter temperature"))
        self.intime = input("Enter intime")
        self.outtime = input("Enter outtime")


class DB:
    def __init__(self):
        self.connection = db.connect(user='root', password='Diksh@#107',
                                  host='127.0.0.1',
                                  database='dikshadb')

        self.cursor = self.connection.cursor()
        print("[DB] Connection Established")

    def execute_sql_query(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DB] SQL Executed")

    def __del__(self):
        self.connection.close()
        print("[DB] Connection Released")




def main():


    # object created
    my_db = DB()

    while True:
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Fetch Customers")
        print("5. To Quit ")

        choice = int(input("Enter Choice"))

        if choice == 1:
            customer = Customer()
            sql = "insert into Customer values(null, '{name}','{phone}','{email}',{temperature},'{intime}','{outtime}')".format_map(vars(customer))

            # here sql statement is passed as parameter,bcz sql statement is to be executed.
            my_db.execute_sql_query(sql)

        elif choice == 5:

          break
    del my_db


if __name__ == '__main__':
    main()
