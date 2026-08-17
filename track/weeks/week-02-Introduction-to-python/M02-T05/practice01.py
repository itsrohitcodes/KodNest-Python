# Build a Book Class

# Define a class named Book
class Book:
    def __init__(self, title, author, price):
        # Store the received values inside the object
        self.title = title
        self.author = author
        self.price = price

# Get the inputs
title = input().strip()
author = input().strip()
price = int(input())

# Create a book object
book = Book(title, author, price)

# Print the book details
print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")