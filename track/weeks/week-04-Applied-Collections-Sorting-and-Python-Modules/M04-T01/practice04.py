# Find Book Details using an ISBN

def find_book(books, isbn):
    # Write your dictionary lookup logic here
    return books.get(isbn)


books = {
    "97801": {"title": "Clean Code", "author": "Robert Martin"},
    "97802": {"title": "Python Crash Course", "author": "Eric Matthes"},
    "97803": {"title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    "97804": {"title": "Algorithms", "author": "Robert Sedgewick"}
}

isbn = input()
book = find_book(books, isbn)

if book is None:
    print("Book not found")
else:
    print(book["title"])
    print(book["author"])