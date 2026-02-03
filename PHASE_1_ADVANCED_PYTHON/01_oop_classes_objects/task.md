# Task: Create a Book and Library System

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create a Book Class
Create a `Book` class with the following:
- Attributes: `title`, `author`, `isbn`, `is_available` (default True)
- Method: `borrow()` - sets `is_available` to False
- Method: `return_book()` - sets `is_available` to True
- Method: `get_info()` - returns a formatted string with book information

## Goal 2: Create a Library Class
Create a `Library` class with the following:
- Attribute: `books` (a list to store Book objects)
- Method: `add_book(book)` - adds a book object to the library
- Method: `list_available_books()` - prints all available books
- Method: `find_book_by_title(title)` - searches and returns a book object

## Goal 3: Test Your Classes
Create a library, add at least 3 books, borrow one book, and list all available books.

---

**Expected Output:**
When you run the code, the terminal should show something like:
```text
Adding books to library...
Available books:
- Python Crash Course by Eric Matthes (ISBN: 123)
- Clean Code by Robert Martin (ISBN: 456)
- FastAPI for Beginners by John Doe (ISBN: 789)

Borrowing 'Clean Code'...
Available books after borrowing:
- Python Crash Course by Eric Matthes (ISBN: 123)
- FastAPI for Beginners by John Doe (ISBN: 789)
```
