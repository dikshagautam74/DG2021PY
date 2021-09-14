# pip install pymongo
# pip install pymongo[srv]

"""
    MongoDB -> Database
    1. Create a Cluster (Free Tier)
    2. Network Settings -> We can connect from any IP Address or some selected range
                        -> 0.0.0.0/0
                        (Security > Network Access)
    3. In the cluster, we can browse collections
        And to create collections, now we need to create a database with collection name
    4. Create Documents in Collections

    MongoDB
        stores data as Collection of Documents
        consider collection as table
        and document as rows. but document is a dictionary here :)
    CRUD Operations with MongoDB
    We will Use pymongo library to perform DB operations
    pip install pymongo -> use -> pip install 'pymongo[srv]'
"""

import pymongo
print(pymongo.__version__)   # gives the version of pymongo installed


# this is the code directly taken from mongodb website,when we choose connect with application
# For making Connection with MongoDB
# We need to have a username and password
# Create Your Username and Password in DataBase Access of MongoDB Console Page | Security > DataBase Access
client = pymongo.MongoClient("mongodb+srv://diksha:<password>@cluster0.1x52c.mongodb.net/gw2021py1?retryWrites=true&w=majority")
db = client.test
print(db)
print(type(db))


