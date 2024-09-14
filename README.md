# Library Management System

A simple library management system built in Python that allows Librarians and Members to manage books within a library. The system supports adding, updating, deleting, borrowing, and returning books, and keeps track of total users and books.

## Features

- **User Management**:
  - Librarians and Members can be registered.
  - Track total number of users via the `get_total_users()` class method.
  
- **Book Management** (Librarians only):
  - Add new books to the library.
  - Update existing book information (title, author).
  - Delete books from the library.
  - View the total number of books via the `get_total_books()` class method.
  
- **Borrowing and Returning Books** (Members only):
  - Members can borrow available books.
  - Members can return borrowed books.
  
- **File Storage**:
  - Books and users are persisted in text files (`books.txt` and `users.txt`).
  - When books or users are added/modified, changes are automatically saved.

## Classes

### 1. `User`
Represents a basic user in the system. Tracks user ID, name, and email. It also keeps a count of total users.

#### Methods:
- `get_total_users(cls)`: Returns the total number of users.
- `display_info(self)`: Displays user's ID, name, and email.

### 2. `Librarian` (inherits from `User`)
A special type of user that can manage books.

#### Methods:
- `add_book(library_manager, book_id, title, author)`: Adds a new book to the library.
- `update_book(library_manager, book_id, new_title, new_author)`: Updates an existing book's information.
- `delete_book(library_manager, book_id)`: Deletes a book from the library.

### 3. `Member` (inherits from `User`)
A regular user who can borrow and return books.

#### Methods:
- `borrow_book(library_manager, book_id)`: Borrows a book from the library.
- `return_book(library_manager, book_id)`: Returns a borrowed book to the library.

### 4. `Book`
Represents a book in the library.

#### Methods:
- `get_total_books(cls)`: Returns the total number of books in the library.
- `display_info(self)`: Displays the book's ID, title, author, and availability.

### 5. `LibraryManager`
Manages the overall library system, including books and users.

#### Methods:
- `add_book(book)`: Adds a new book to the library.
- `update_book(book_id, new_title, new_author)`: Updates a book's information.
- `delete_book(book_id)`: Deletes a book from the library.
- `borrow_book(book_id, member_id)`: Allows a member to borrow a book.
- `return_book(book_id, member_id)`: Allows a member to return a borrowed book.
- `load_books()`: Loads books from `books.txt`.
- `save_books()`: Saves books to `books.txt`.
- `load_users()`: Loads users from `users.txt`.
- `save_users()`: Saves users to `users.txt`.

## How to Use

1. **Register Users**: Register a librarian or a member by choosing the respective option in the menu.
2. **Manage Books** (Librarian only):
   - Add new books.
   - Update or delete existing books.
3. **Borrow and Return Books** (Member only):
   - Members can borrow available books.
   - Members can return books that were borrowed.
4. **View Books**: Display the list of all books in the library.

## Running the Program

To run the Library Management System, simply execute the `manage_library()` function:

```bash
python library_management.py
