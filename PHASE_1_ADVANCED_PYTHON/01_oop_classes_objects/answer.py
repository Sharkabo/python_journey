# My Answer for Unit 01: Classes and Objects

# Write your code here
class Book:
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True):
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.is_available: bool = is_available
    
    def borrow(self) -> None:
        self.is_available = False
    
    def return_book(self) -> None:
        self.is_available = True
    
    def get_info(self) -> str:
        if self.is_available:
            return f'{self.title} is written by {self.author}, it\'s ISBN code is {self.isbn}, available to borrow.'
        else:
            return f'{self.title} is written by {self.author}, it\'s ISBN code is {self.isbn}, not available to borrow.'
        
class Library:
    def __init__(self):
        self.books: list[Book] = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print('Successfully added!')
    
    def list_available_books(self) -> None:
        available: list[Book] = [book for book in self.books if book.is_available]
        if not available:
            print('No book is available')
        else:
            print('Available books:')
            for book in available:
                print(f'- {book.title} by {book.author} (ISBN: {book.isbn})')
    
    def find_book_by_title(self, title : str) -> Book | None:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

library = Library()

while True:
    input_choice = input('Please select your action:\n1. Add book\n2. List All available books\n3. Find a book by the title\n4. Borrow the book by the title\n5. Exit the menu\n')
    try:
        choice = int(input_choice)
    except ValueError:
        print('Please input the number on the menu')
        break

    match choice:
        case 5:
            break
        case 1:
            title = input('Please input the title:')
            author = input('Please input the author:')
            isbn = input('Please input the ISBN code:')
            new_book = Book(title, author, isbn)
            library.add_book(new_book) 
        case 2:
            library.list_available_books()
        case 3:
            input_title = input('Please input the book title you want to find:')
            result = library.find_book_by_title(input_title)
            if result:
                print(f"Found it! {result.get_info()}")
            else:
                print("Sorry, we don't have this book.")
        case 4:
            input_title = input('Please input the book title which you want to borrow:')
            result = library.find_book_by_title(input_title)
            if result is None:
                print('The book you want to borrow doesn\'t exist.')
            elif not result.is_available:
                print(f'Sorry, "{result.title}" is already borrowed by someone else.')
            else:
                result.borrow()
                print(f'Successfully borrowed "{result.title}"! Enjoy your reading.')