"""Custom exceptions for the library system."""


class LibraryError(Exception):
    """Base error for anything going wrong in the library."""
    pass


class BookNotFoundError(LibraryError):
    """Raised when a book doesn't exist in our catalog."""
    pass


class MemberNotFoundError(LibraryError):
    """Raised when a member ID isn't registered."""
    pass


class OutOfStockError(LibraryError):
    """Raised when all copies of a book are currently borrowed."""
    pass


class IssueError(LibraryError):
    """Raised when an issue or return rule is broken."""
    pass


class ValidationError(LibraryError):
    """Raised when bad input is given (e.g. empty title, bad phone number)."""
    pass