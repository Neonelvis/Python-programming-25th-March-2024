import sqlite3 

# CRUD 
# C - Create -> INSERT INTO ... 
# R - Retrieve/Read -> SELECT ... FROM ... 
# U - Update/Modify/Edit -> UPDATE ... SET... 
# D - Delete/Drop -> DELETE FROM ... 

# Step 1 : Import the sqlite3 module 
# Step 2 : Create a Database and connection to the database 
# Step 3: Perform SQL stuff (CRUD)

database = 'shop.db'

# Create connection 
connection = sqlite3.connect(database)

# function to create a table 
def create_table():
    # create table sql query (SQL STATEMENT)
    query = """CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER UNIQUE NOT NULL PRIMARY KEY, 
        name char(20),
        quantity INTEGER, 
        price REAL 
    );"""
    # create a cursor object 
    cursor = connection.cursor()
    # use the cursor to execute the create table query 
    cursor.execute(query) 
    # commit/save changes to the DB 
    connection.commit() 
    # close the connection to the db 
    connection.close()  

# Perform CRUD 
# create_table()      

# 1. C - Create a product 
def create_product(): 
    # create the insert query 
    query = "INSERT INTO products (name, quantity, price) VALUES ('Product-3', 3, 19.99)" 
    # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query)
    # commit changes 
    connection.commit() 
    # close the connection 
    connection.close() 

# create_product()

# 2. R - Read - View/Read One Product 
def read_one_product():
    # create the select one query 
    query = "SELECT * FROM products WHERE product_id = ?"
    # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query, [1])
    # fetch all products and store them in a products variable 
    product = cursor.fetchone() 
    # close the DB connection
    connection.close() 
    # return the products list  
    # display all the product
    print(f"{product[0]}. Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")

# read_one_product()

# 2. R - Read - View/Read Many Products  
def read_products():
    # create the select one query 
    query = "SELECT * FROM products"
    # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query) 
    # fetch all products and store them in a products variable 
    products = cursor.fetchall() 
    # close the DB connection
    connection.close() 
    # return the products list 
    # print(products) 
    # display all the products 
    for product in products: 
        print(f"{product[0]}. Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")

# read_products()

# 3. U - Update a Product 
def update_product():
    # create the update query 
    query = "UPDATE products SET quantity = ? WHERE product_id = ?"
     # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query, [53, 3])
     # commit changes 
    connection.commit() 
    # close the connection 
    connection.close()

# update_product()

# 4. Delete a Product
def delete_one_product():
    # create the update query 
    query = "DELETE FROM products WHERE product_id = ?"
     # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query, [3])
     # commit changes 
    connection.commit() 
    # close the connection 
    connection.close()

# delete_one_product()

# 4. Delete all products
def delete_all_products():
     # create the update query 
    query = "DELETE FROM products"
     # create the cursor object 
    cursor = connection.cursor() 
    # execute the query 
    cursor.execute(query)
     # commit changes 
    connection.commit() 
    # close the connection 
    connection.close()

delete_all_products()