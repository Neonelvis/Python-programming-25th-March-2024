# Create a path to our books text file 
file_path = 'books.txt' 

# create a function to add a book into the books text file 
def add_book(title, author):
    with open(file_path, 'a') as file:
        new_book = f"{title},{author},0\n"
        file.write(new_book)
        # file.write(f"{title},{author},0\n")

# create a function to display all the books 
def get_all_books():
    with open(file_path, 'r') as file:
        all_books = [book.strip('\n').split(',') for book in file.readlines()] 
        
        books = [
            {'title': book[0], 'author': book[1], 'read': book[2]} 
            for book in all_books
        ]

        return books 

# create a function to mark a book as read 
def mark_book_as_read(title):
    book = get_all_books()
    for book in books:
        if book['title'].lower() == title.lower():
            book['read'] = 'l' 
    # create a helper function to save the books in the file 
    _save_all_books(books)

def _save_all_books(books):
    with open(file_path, 'w') as file:
        for book in books: 
            file.write(f"{book['title']},{book['author']},{book['read']}\n ")

# create a function to delete a book 
def delete_book(title): 
    books = get_all_books() 
    books = [book for book in books if book['title'].lower() != title.lower()]
    _save_all_books(books)