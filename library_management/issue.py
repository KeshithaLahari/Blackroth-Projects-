"""Track book checkouts, returns, and calculate overdue fines."""

from datetime import datetime, timedelta
from library_management.book import BookManager
from library_management.exceptions import (
    IssueError,
    OutOfStockError,
    ValidationError,
)
from library_management.member import MemberManager
from library_management.storage import JSONStorage


class IssueRecord:
    """Represents a single book issue transaction."""

    def __init__(
        self,
        issue_id: str,
        book_id: str,
        member_id: str,
        issue_date: str,
        due_date: str,
        return_date: str = None,
        fine_paid: float = 0.0,
    ) -> None:
        self.issue_id = issue_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine_paid = fine_paid

    @property
    def is_returned(self) -> bool:
        """Check if the book has been returned."""
        return self.return_date is not None

    def to_dict(self) -> dict:
        """Convert issue record into a dictionary for JSON."""
        return {
            "issue_id": self.issue_id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "issue_date": self.issue_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "fine_paid": self.fine_paid,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "IssueRecord":
        """Recreate an IssueRecord from JSON dictionary."""
        return cls(
            issue_id=data["issue_id"],
            book_id=data["book_id"],
            member_id=data["member_id"],
            issue_date=data["issue_date"],
            due_date=data["due_date"],
            return_date=data.get("return_date"),
            fine_paid=data.get("fine_paid", 0.0),
        )


class IssueManager:
    """Handles lending books, receiving returns, and charging fines."""

    FINE_PER_DAY = 5.0
    LOAN_DAYS = 14

    def __init__(
        self,
        storage: JSONStorage,
        filepath: str,
        book_manager: BookManager,
        member_manager: MemberManager,
    ) -> None:
        self.storage = storage
        self.filepath = filepath
        self.book_manager = book_manager
        self.member_manager = member_manager
        self.issues: list[IssueRecord] = [
            IssueRecord.from_dict(d) for d in self.storage.load(filepath)
        ]

    def _save(self) -> None:
        """Helper to save issues back to JSON."""
        self.storage.save(self.filepath, [i.to_dict() for i in self.issues])

    def issue_book(self, book_id: str, member_id: str) -> IssueRecord:
        """Borrow an available book."""
        book = self.book_manager.find_by_id(book_id)
        member = self.member_manager.find_by_id(member_id)

        if not member.is_active:
            raise ValidationError("This member account is inactive.")

        if book.available_copies <= 0:
            raise OutOfStockError("No copies available for checkout right now.")

        # Prevent duplicate active issues of the same book
        for active in self.issues:
            if (
                active.book_id == book.book_id
                and active.member_id == member.member_id
                and not active.is_returned
            ):
                raise IssueError("Member already holds an unreturned copy of this book.")

        now = datetime.now()
        due = now + timedelta(days=self.LOAN_DAYS)
        issue_id = f"ISSUE{len(self.issues) + 1:04d}"

        record = IssueRecord(
            issue_id=issue_id,
            book_id=book.book_id,
            member_id=member.member_id,
            issue_date=now.strftime("%Y-%m-%d"),
            due_date=due.strftime("%Y-%m-%d"),
        )

        book.available_copies -= 1
        self.book_manager._save()
        self.issues.append(record)
        self._save()
        return record

    def return_book(self, issue_id: str) -> tuple[IssueRecord, float]:
        """Process return, compute late fine if overdue, and increment copies."""
        clean_id = issue_id.strip().upper()
        record = None
        for item in self.issues:
            if item.issue_id == clean_id:
                record = item
                break

        if not record:
            raise IssueError(f"Issue record '{issue_id}' not found.")
        if record.is_returned:
            raise IssueError("This book is already marked as returned.")

        now = datetime.now()
        record.return_date = now.strftime("%Y-%m-%d")
        due = datetime.strptime(record.due_date, "%Y-%m-%d")

        fine = 0.0
        if now > due:
            days_late = (now - due).days
            fine = float(days_late * self.FINE_PER_DAY)

        record.fine_paid = fine

        book = self.book_manager.find_by_id(record.book_id)
        book.available_copies = min(book.total_copies, book.available_copies + 1)
        self.book_manager._save()
        self._save()

        return record, fine