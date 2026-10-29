"""Book models and book catalog management operations."""

from typing import Any

from exceptions import BookNotFoundError, BookUnavailableError, ValidationError
from storage import JSONStorage
from validator import validate_non_empty, validate_positive_int


class Book:
    """Represent a single book entity in the catalog."""

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        total_copies: int,
        borrowed_copies: int = 0,
    ) -> None:
        """Initialize a book instance."""
        self.book_id = validate_positive_int(book_id, "Book ID")
        self.title = validate_non_empty(title, "Title")
        self.author = validate_non_empty(author, "Author")
        self.total_copies = validate_positive_int(total_copies, "Total Copies")
        self.borrowed_copies = borrowed_copies

    @property
    def available_copies(self) -> int:
        """Return the number of available copies for borrowing."""
        return max(self.total_copies - self.borrowed_copies, 0)

    def to_dict(self) -> dict[str, Any]:
        """Convert the book object to a JSON-compatible dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "borrowed_copies": self.borrowed_copies,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Book":
        """Build a Book instance from stored dictionary data."""
        return cls(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            total_copies=data["total_copies"],
            borrowed_copies=data.get("borrowed_copies", 0),
        )


class BookManager:
    """Manage the book catalog with JSON persistence."""

    def __init__(self, filename: str = "books.json") -> None:
        """Initialize book management with JSON storage."""
        self.storage = JSONStorage(filename)

    def _load_books(self) -> list[Book]:
        """Load all books from storage."""
        return [Book.from_dict(record) for record in self.storage.load()]

    def _save_books(self, books: list[Book]) -> None:
        """Save all books to storage."""
        self.storage.save([book.to_dict() for book in books])

    def add_book(
        self,
        book_id: int,
        title: str,
        author: str,
        total_copies: int,
    ) -> Book:
        """Add a new book to the catalog."""
        books = self._load_books()

        if any(book.book_id == book_id for book in books):
            raise ValidationError(f"Book ID {book_id} already exists.")

        book = Book(book_id, title, author, total_copies)
        books.append(book)
        self._save_books(books)
        return book

    def get_book(self, book_id: int) -> Book:
        """Find a book by its numeric ID."""
        validate_positive_int(book_id, "Book ID")
        for book in self._load_books():
            if book.book_id == book_id:
                return book

        raise BookNotFoundError(f"Book ID {book_id} was not found.")

    def search_books(self, query: str) -> list[Book]:
        """Search books by title or author."""
        query = validate_non_empty(query, "Search query").casefold()
        return [
            book
            for book in self._load_books()
            if query in book.title.casefold() or query in book.author.casefold()
        ]

    def change_borrowed_copies(self, book_id: int, change: int) -> None:
        """Increment or decrement borrowed copies upon issue or return."""
        books = self._load_books()
        for book in books:
            if book.book_id == book_id:
                new_borrowed = book.borrowed_copies + change
                if new_borrowed < 0 or new_borrowed > book.total_copies:
                    raise BookUnavailableError("Invalid copy count adjustment.")
                book.borrowed_copies = new_borrowed
                self._save_books(books)
                return

        raise BookNotFoundError(f"Book ID {book_id} was not found.")

    def list_books(self) -> list[Book]:
        """Return all books in the catalog."""
        return self._load_books()