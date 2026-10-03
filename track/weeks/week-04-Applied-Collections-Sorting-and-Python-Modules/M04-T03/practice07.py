# Sort Books According to Their Page Count

n = int(input())
books = []

for _ in range(n):
    book_name, page_count = input().split()
    books.append((book_name, int(page_count)))

# Write your code here
sorted_books = sorted(books, key = lambda i : i[1])

for name, count in sorted_books:
    print(name, count)