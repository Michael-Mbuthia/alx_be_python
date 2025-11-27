class Book:
    def __init__(self, title, author):
        self.title = title                     # Public attribute
        self.author = author                   # Public attribute
        self._is_checked_out = False           # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []   # Private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                book.check_out()
                return
        print(f"Book titled '{title}' not found.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f"Book titled '{title}' not found.")

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
