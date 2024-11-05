class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def display_details(self):
        status = "Available" if self.available else "Checked Out"
        return f"{self.title} by {self.author}, Genre: {self.genre}, Status: {status}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed: {title}")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.display_details()
        return "Book not found."

    def display_available_books(self):
        available_books = [book.display_details() for book in self.books if book.available]
        return available_books if available_books else ["No books available"]

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You borrowed: {title}")
                    return
                else:
                    print("Book is already checked out.")
                    return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.available = True
                print(f"You returned: {title}")
                return
        print("Book not found.")


def main():
    library = LibraryCatalog()

    while True:
        print("\nLibrary System Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Available Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            library.add_book(Book(title, author, genre))

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter the title to search: ")
            print(library.search_book(title))

        elif choice == '4':
            for book in library.display_available_books():
                print(book)

        elif choice == '5':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == '6':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
