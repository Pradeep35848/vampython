import os

class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Quantity: {self.quantity}"

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, title, author, isbn, quantity):
        book = Book(title, author, isbn, quantity)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently unavailable.")
                    return
        print("Book not found in the library.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += 1
                print(f"You have returned '{book.title}'.")
                return
        print("This book was not borrowed from this library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            quantity = int(input("Enter quantity: "))
            library.add_book(title, author, isbn, quantity)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            isbn = input("Enter the ISBN of the book to borrow: ")
            library.borrow_book(isbn)

        elif choice == '4':
            isbn = input("Enter the ISBN of the book to return: ")
            library.return_book(isbn)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
