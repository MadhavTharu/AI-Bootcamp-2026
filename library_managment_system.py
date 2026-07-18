# simple Library Management System in Python 

# Add new books to the library
# Remove books from the library
# Search books by title or author
# Display all available books

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = {
            "title": title,
            "author": author
        }

        self.books.append(book)
        print("\nBook added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")

        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print("\nBook removed successfully!\n")
                return

        print("\nBook not found!\n")

    def search_book(self):
        keyword = input("Enter title or author to search: ").lower()

        found = False
        print("\nSearch Results:")
        print("-" * 30)

        for book in self.books:
            if keyword in book["title"].lower() or keyword in book["author"].lower():
                print(f"Title : {book['title']}")
                print(f"Author: {book['author']}")
                print("-" * 30)
                found = True

        if not found:
            print("No matching books found.")

        print()

    def display_books(self):
        if not self.books:
            print("\nNo books available in the library.\n")
            return

        print("\nAvailable Books")
        print("-" * 30)

        for i, book in enumerate(self.books, start=1):
            print(f"{i}. Title : {book['title']}")
            print(f"   Author: {book['author']}")
            print("-" * 30)


library = Library()

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.remove_book()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.\n")