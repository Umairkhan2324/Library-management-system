from typing import List, Union
class User:
    _total_users = 0
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        User._total_users += 1

    @classmethod
    def get_total_users(cls) -> int:
        return cls._total_users

    def display_info(self) -> None:
        print(f"User ID: {self._user_id}, Name: {self._name}, Email: {self._email}")
class Librarian(User):
    def add_book(self, library_manager, book_id: int, title: str, author: str) -> None:
        library_manager.add_book(Book(book_id, title, author, True))

    def update_book(self, library_manager, book_id: int, new_title: str, new_author: str) -> None:
        library_manager.update_book(book_id, new_title, new_author)

    def delete_book(self, library_manager, book_id: int) -> None:
        library_manager.delete_book(book_id)
class Member(User):
    def borrow_book(self, library_manager, book_id: int) -> None:
        library_manager.borrow_book(book_id, self._user_id)
    def return_book(self, library_manager, book_id: int) -> None:
        library_manager.return_book(book_id, self._user_id)
class Book:
    _total_books = 0
    def __init__(self, book_id: int, title: str, author: str, availability: bool):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability
        Book._total_books += 1
    @classmethod
    def get_total_books(cls) -> int:
        return cls._total_books
    def display_info(self) -> None:
        status = "Available" if self._availability else "Not Available"
        print(f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {status}")
class LibraryManager:
    books_file = 'books.txt'
    users_file = 'users.txt'
    def __init__(self):
        self.books = self.load_books()
        self.users = self.load_users()
    def add_book(self, book: Book) -> None:
        if any(b._book_id == book._book_id for b in self.books):
            print(f"Book with ID {book._book_id} already exists.")
        else:
            self.books.append(book)
            self.save_books()
            print(f"Book '{book._title}' added to the library.")
    def update_book(self, book_id: int, new_title: str, new_author: str) -> None:
        for book in self.books:
            if book._book_id == book_id:
                book._title = new_title
                book._author = new_author
                self.save_books()
                print(f"Book {book_id} updated.")
                break
        else:
            print(f"Book {book_id} not found.")
    def delete_book(self, book_id: int) -> None:
        initial_len = len(self.books)
        self.books = [book for book in self.books if book._book_id != book_id]
        if len(self.books) < initial_len:
            self.save_books()
            print(f"Book {book_id} deleted.")
        else:
            print(f"Book with ID {book_id} not found.")
    def borrow_book(self, book_id: int, member_id: int) -> None:
        for book in self.books:
            if book._book_id == book_id:
                if book._availability:
                    book._availability = False
                    self.save_books()
                    print(f"Book '{book._title}' has been borrowed by member {member_id}.")
                else:
                    print(f"Book '{book._title}' is currently unavailable.")
                return
        print(f"Book with ID {book_id} not found.")
    def return_book(self, book_id: int, member_id: int) -> None:
        for book in self.books:
            if book._book_id == book_id:
                if not book._availability:
                    book._availability = True
                    self.save_books()
                    print(f"Book '{book._title}' has been returned by member {member_id}.")
                else:
                    print(f"Book '{book._title}' was not borrowed.")
                return
        print(f"Book with ID {book_id} not found.")
    def load_books(self) -> List[Book]:
        books = []
        try:
            with open(self.books_file, 'r') as f:
                for line in f:
                    book_data = line.strip().split(',')
                    book = Book(int(book_data[0]), book_data[1], book_data[2], book_data[3] == 'True')
                    books.append(book)
        except FileNotFoundError:
            print(f"{self.books_file} not found. Starting with an empty book list.")
        return books
    def save_books(self) -> None:
        with open(self.books_file, 'w') as f:
            for book in self.books:
                f.write(f"{book._book_id},{book._title},{book._author},{book._availability}\n")
    def load_users(self) -> List[Union[Librarian, Member]]:
        users = []
        try:
            with open(self.users_file, 'r') as f:
                for line in f:
                    user_data = line.strip().split(',')
                    if user_data[3] == "Librarian":
                        user = Librarian(int(user_data[0]), user_data[1], user_data[2])
                    else:
                        user = Member(int(user_data[0]), user_data[1], user_data[2])
                    users.append(user)
        except FileNotFoundError:
            print(f"{self.users_file} not found. Starting with an empty user list.")
        return users
    def save_users(self) -> None:
        with open(self.users_file, 'w') as f:
            for user in self.users:
                user_type = 'Librarian' if isinstance(user, Librarian) else 'Member'
                f.write(f"{user._user_id},{user._name},{user._email},{user_type}\n")
def register_user(manager: LibraryManager, user_type: str) -> None:
    user_id = int(input("Enter user ID: "))
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    if user_type == "Librarian":
        user = Librarian(user_id, name, email)
    else:
        user = Member(user_id, name, email)
    manager.users.append(user)
    manager.save_users()
    print(f"{user_type} '{name}' registered successfully.")
def display_books(manager: LibraryManager) -> None:
    print("\nBooks in the library:")
    for book in manager.books:
        book.display_info()
def manage_library():
    manager = LibraryManager()
    while True:
        print("\n--- Library Management System ---")
        print("1. Register a Librarian")
        print("2. Register a Member")
        print("3. Add a Book (Librarian only)")
        print("4. Update a Book (Librarian only)")
        print("5. Delete a Book (Librarian only)")
        print("6. Borrow a Book (Member only)")
        print("7. Return a Book (Member only)")
        print("8. Display All Books")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user(manager, "Librarian")
        elif choice == "2":
            register_user(manager, "Member")
        elif choice == "3":
            librarian_id = int(input("Enter Librarian ID: "))
            for user in manager.users:
                if isinstance(user, Librarian) and user._user_id == librarian_id:
                    book_id = int(input("Enter Book ID: "))
                    title = input("Enter Book Title: ")
                    author = input("Enter Book Author: ")
                    user.add_book(manager, book_id, title, author)
                    break
            else:
                print("Invalid Librarian ID.")
        elif choice == "4":
            librarian_id = int(input("Enter Librarian ID: "))
            for user in manager.users:
                if isinstance(user, Librarian) and user._user_id == librarian_id:
                    book_id = int(input("Enter Book ID to update: "))
                    new_title = input("Enter new title: ")
                    new_author = input("Enter new author: ")
                    user.update_book(manager, book_id, new_title, new_author)
                    break
            else:
                print("Invalid Librarian ID.")
        elif choice == "5":
            librarian_id = int(input("Enter Librarian ID: "))
            for user in manager.users:
                if isinstance(user, Librarian) and user._user_id == librarian_id:
                    book_id = int(input("Enter Book ID to delete: "))
                    user.delete_book(manager, book_id)
                    break
            else:
                print("Invalid Librarian ID.")
        elif choice == "6":
            member_id = int(input("Enter Member ID: "))
            for user in manager.users:
                if isinstance(user, Member) and user._user_id == member_id:
                    book_id = int(input("Enter Book ID to borrow: "))
                    user.borrow_book(manager, book_id)
                    break
            else:
                print("Invalid Member ID.")
        elif choice == "7":
            member_id = int(input("Enter Member ID: "))
            for user in manager.users:
                if isinstance(user, Member) and user._user_id == member_id:
                    book_id = int(input("Enter Book ID to return: "))
                    user.return_book(manager, book_id)
                    break
            else:
                print("Invalid Member ID.")
        elif choice == "8":
            display_books(manager)
        elif choice == "9":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    manage_library()
