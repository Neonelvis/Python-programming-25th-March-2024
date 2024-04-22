# import sqlite3 module 
import sqlite3 

# bookstore database 
db = 'bookstore.db'

# a function to create the books table 
def create_books_table():
    # create the database connection 
    connection = sqlite3.connect(db)
    # create the create table query 
    query = """CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER UNIQUE NOT NULL PRIMARY KEY,
        title char(50),
        author char(50), 
        read INTEGER NOT NULL 
    );""" 
    # create the cursor object 
    cursor = connection.cursor()
    # execute the query 
    cursor.execute(query)
    # commit the changes
    connection.commit()
    # close the db connection 
    connection.close()

# create a function to add a book into the books text file 
def add_book(title, author):
    # create the database connection 
    connection = sqlite3.connect(db)
    # create the add book query 
    query = "INSERT INTO books(title, author, read) VALUES (?,?,?)" 
    # create the cursor object 
    cursor = connection.cursor()
    # execute the query 
    cursor.execute(query, [title, author, 0])
    # commit the changes
    connection.commit()
    # close the db connection 
    connection.close()



# create a function to display all the books 
def get_all_books():
    # create the database connection 
    connection = sqlite3.connect(db)
    # create the add book query 
    query = "SELECT * FROM books" 
    # create the cursor object 
    cursor = connection.cursor()
    # execute the query 
    cursor.execute(query)
    # retrieve/read all books from db 
    books = cursor.fetchall()
    # close the db connection 
    connection.close()
    # return the books list 
    return books 



# create a function to mark a book as read 
def mark_book_as_read(title):
    # create the database connection 
    connection = sqlite3.connect(db)
    # create the update book query 
    query = "UPDATE books SET read = ? WHERE title = ? " 
    # create the cursor object 
    cursor = connection.cursor()
    # execute the query 
    cursor.execute(query, [1, title])
    # commit the changes
    connection.commit()
    # close the db connection 
    connection.close()


def _save_all_books(books):
    with open(file_path, 'w') as file:
        for book in books: 
            file.write(f"{book['title']},{book['author']},{book['read']}\n ")

# create a function to delete a book 
def delete_book(title): 
    # create the database connection 
    connection = sqlite3.connect(db)

    # check if the book title exists 
    books = get_all_books()

    for book in books:
        if book[1] == title:
            # create the delete query 
            query = "DELETE FROM books WHERE title = ?"
            # create a cursor
            cursor = connection.cursor() 
            # execute the delete query 
            cursor.execute(query, [title]) 
            # commit changes 
            connection.commit() 
            # close the connection 
            connection.close() 
            print(f"Book with title {book[1]} has been deleted successfully.") 
        print(f"Book with name {book[1]} does not exist in our DB")

    
    