class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List of books in the library
        self.borrowed_books = {}  # Tracks borrowed books and borrowers

    def add_book(self, book_name):
        """Adds a book to the library."""
        self.books.append(book_name)
        print(f"📚 '{book_name}' has been added to the library.")

    def display_books(self):
        """Displays all available books in the library."""
        if self.books:
            print(f"\n📖 Available books in {self.name}:")
            for index, book in enumerate(self.books, 1):
                print(f"{index}. {book}")
        else:
            print("❌ No books are currently available in the library.")

    def borrow_book(self, book_name, borrower_name):
        """Allows a user to borrow a book."""
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books[book_name] = borrower_name
            print(f"✅ '{book_name}' has been borrowed by {borrower_name}.")
        elif book_name in self.borrowed_books:
            print(f"❌ '{book_name}' is already borrowed by {self.borrowed_books[book_name]}.")
        else:
            print(f"❌ '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        """Allows a user to return a borrowed book."""
        if book_name in self.borrowed_books:
            borrower_name = self.borrowed_books.pop(book_name)
            self.books.append(book_name)
            print(f"✅ '{book_name}' has been returned by {borrower_name}.")
        else:
            print(f"❌ '{book_name}' was not borrowed from the library.")

# Main program
def main():
    library = Library("Central Library")

    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                book_name = input("Enter the name of the book to add: ").strip()
                library.add_book(book_name)
            elif choice == 2:
                library.display_books()
            elif choice == 3:
                book_name = input("Enter the name of the book to borrow: ").strip()
                borrower_name = input("Enter your name: ").strip()
                library.borrow_book(book_name, borrower_name)
            elif choice == 4:
                book_name = input("Enter the name of the book to return: ").strip()
                library.return_book(book_name)
            elif choice == 5:
                print("📚 Thank you for using the Library Management System!")
                break
            else:
                print("❌ Invalid choice. Please select a valid option.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
