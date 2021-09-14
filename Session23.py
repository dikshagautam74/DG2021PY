"""
    Persistence:
    1. Files
    2. DataBases
        MySQL       | SQL
        MongoDB     | NoSQL         (APIs)
        Google -> FirebaseFirestore | NoSQL   (APIs)
    Lets Start with MySQL
    1. Installation
        1.1 Direct MySQL DB (https://dev.mysql.com/downloads/installer/)
        1.2 XAMPP -> apachefriends website
    2. Path Setup
    3. Execute commands on shell/terminal
    4. MySQL Uses SQL Language
        SQL -> Commands as good as english sentences with ; as terminating statement
"""
# in python by default every class we create is child of a built in class called object
# class ProductInventory(object):

"""
    DataBase: is a collection of tables
    Table: is a collection of Rows and Columns
          where columns are the headers and Rows are the data


    ORM: Object Relational Mapping
         Structure of Object is Structure of Table 

     # this piece of code directly executed in the mysql,but to execute this same code in python we have
      to make sql statements and that piece of code will be adde din the table made by this code.   
    create table ProductInventory(
        id int primary key auto_increment,  -> primary key means if value of id is given once,can't be changed;and auto_increment means value will start from 1 and gets incremented automatically in rows
        name varchar(256),
        quantity int,
        location varchar(256)
    )

    Commands for using database:
    create database any_name;
    show databases;
    show tables;

    SQL CRUD Operations: CRUD -> create,retrieve,update and delete

    Insert:
    insert into ProductInventory values(null, 'Maggi', 11, 'cupboard1')

    Update:
    # u have to write the update data in single quotes 
    update ProductInventory set name = 'Maggi Atta', quantity = 15

    Delete:
    delete from ProductInventory where id = 1

    Fetch
    select * from ProductInventory
    select * from ProductInventory where id = 1
    select * from ProductInventory where id = 1 and name = "Maggie"
    select * from ProductInventory where id = 1 and quantity < 5
    select * from ProductInventory where quantity < 2

"""
# import statement for accessing sql conncector package,db is the short name(alias) for this.
import mysql.connector as db


class ProductInventory:

    def __init__(self, id=0, name=None, quantity=0, location=None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.location = location

    # def __str__(self):
    #     return "{id},{name},{quantity},{location}\n".format_map(vars(self))

    #  we can write repr statement here also in str,it will do the work of repr
    #   return "productInventory({id},{name},{quantity},{location})".format_map(vars(self))

    # both str and repr works same but repr gives us the representation of object with the class name specified
    def __repr__(self):
        return "ProductInventory(id={id},name={name},quantity={quantity},location={location})\n".format_map(vars(self))


def main():
    product1 = ProductInventory(name="Pizza", quantity=1, location="cupboard2")
    print(product1)
    #
    # del product1

    # 1. Create Connection to DataBase,this code snippet  is fixed
    connection = db.connect(user='root', password='Diksh@#107',
                            host='127.0.0.1',
                            database='dikshadb')

    print("Connection Created", connection, type(connection))

    # this is the sql statement we want to execute
    # here id is assigned as null bcoz we have mentioned auto-increment above,so it will be incremented automatically.
    sql = "insert into ProductInventory values(null, '{name}', {quantity}, '{location}')".format_map(vars(product1))
    print(sql)

    # # 2. Obtain Cursor to Database for executing SQL Instructions
    cursor = connection.cursor()
    #
    # # 3. Execute SQL Statement
    cursor.execute(sql)
    #
    # # 4. Make SQL as a Transaction
    connection.commit()
    # print("Transaction Done :)")

    # 5. Close the Connection
    connection.close()
    print("Connection Closed")

    # u have to write all the elements to add a new row in table in database


if __name__ == '__main__':
    main()