from utils import database

USER_CHOICE ="""
Enter:

- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your Choice:"""

def menu():
    # create the books table 
    database.create_books_table()
    
    user_input = input(USER_CHOICE)
    
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            mark_book_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid choice, please Try again!!!")
        user_input = input(USER_CHOICE)  

# a function to prompt the user to add a new book
def prompt_add_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    database.add_book(title, author)

# a function to list all books
def list_books():
    # get the books count
    books_count = database.count_books()
    # get all the books from the database
    books = database.get_all_books()
    # s variable for the bookscount display logic 
    s = "s" if books_count > 1 or books_count <= 0 else ""
    # display the count to the user
    print(f"You have {books_count} book{s} in your collection.")
    for idx, book in enumerate(books): 
        read = "Yes" if book[3] == 1 else "No"
        print(f"{idx}.{book[1]} written by {book[2]}, read: {read}")

# a function to prompt the user to mark a book as read
def mark_book_as_read():
    title = input("Enter the title of the book you've finished reading: ")
    database.mark_book_as_read(title)
    
# a function to prompt the user to delete a book
def prompt_delete_book():
    title = input("Enter the book you wish to delete: ")
    database.delete_book(title)      
            
# call the menu function
menu()
