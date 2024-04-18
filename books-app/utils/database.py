# create an empty list to store the books
books = [
    {
        'title': 'Clean Code', 
        'author': 'Robert C. Martin',
        'read': False
    },
    {
        'title': 'Modern Javascript', 
        'author': 'Dennis Muthui', 
        'read': False
    }
]

# create a function to add books to the list
def add_book(title, author):
    books.append({
        'title': title,
        'author': author,
        'read': False
    })
    
# create afunction to get all the books from the list
def get_all_books():
    return books

# create a function to mark a book as read
def mark_book_read(title):
    for book in books:
        if book['title'] == title:
            book['read'] = True
# create a function to delete a book
def delete_book(title):
    # for book in books: 
    #     if book['title'] == title:
    #         books.remove(book)
    global books 
    books = [book for book in books if book['title'] != title ]