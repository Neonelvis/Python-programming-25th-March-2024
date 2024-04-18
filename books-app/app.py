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
    user_input = input(USER_CHOICE)
    
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_mark_book_as_read()
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
    books = database.get_all_books()
    for book in  books:
        read_status = "Yes" if book['read'] == True else "No"
        print(f"{book['title']} written by {book['author']}, read: {read_status}")

# a function to prompt the user to mark a book as read
def prompt_mark_book_as_read():
    title = input("Enter the title of the book you've finished reading: ")
    database.mark_book_read(title)
    
# a function to prompt the user to delete a book
def prompt_delete_book():
    title = input("Enter the book you wish to delete: ")
    database.delete_book(title)      
            
# call the menu function
menu()
