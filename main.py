books = ["Python Basics", "Math Magic", "Science World", "English Grammar", "Computer Fun"]
copies = [3, 0, 5, 2, 0]

print("Library Books and Copies")

for book, copy in zip(books, copies):
    print(book, ":", copy)

available = list(filter(lambda x: x[1] > 0, zip(books, copies)))

print("\nAvailable Books:")
for book, copy in available:
    print(book, ":", copy)

late_fees = [10, 20, 15, 30, 25]

updated_fees = list(map(lambda x: x + 5, late_fees))

print("\nUpdated Late Fees:")
print(updated_fees)

print("\nBook Checking")

for book, copy in zip(books, copies):
    print("Checking:", book)

    if copy == 0:
        print(book, "is unavailable.")
        break

    print(book, "is available.")