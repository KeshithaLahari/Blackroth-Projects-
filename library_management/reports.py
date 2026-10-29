"""Reporting tools for library inventory, checkouts, and fines."""

from collections import Counter
from library_management.book import BookManager
from library_management.issue import IssueManager
from library_management.member import MemberManager


class ReportService:
    """Generates clean console reports."""

    def __init__(
        self,
        book_mgr: BookManager,
        member_mgr: MemberManager,
        issue_mgr: IssueManager,
    ) -> None:
        self.book_mgr = book_mgr
        self.member_mgr = member_mgr
        self.issue_mgr = issue_mgr

    def print_inventory(self) -> None:
        """Print full list of books and available copies."""
        print("\n" + "=" * 65)
        print(f"{'ID':<6} {'Title':<25} {'Author':<20} {'Available'}")
        print("=" * 65)
        if not self.book_mgr.books:
            print("No books found in catalog.")
        for b in self.book_mgr.books:
            print(f"{b.book_id:<6} {b.title[:24]:<25} {b.author[:19]:<20} {b.available_copies}/{b.total_copies}")
        print("=" * 65)

    def print_borrowed_books(self) -> None:
        """Print all books that are currently issued and not returned."""
        active = [i for i in self.issue_mgr.issues if not i.is_returned]
        print("\n" + "=" * 60)
        print(f"{'Issue ID':<12} {'Book ID':<10} {'Member ID':<12} {'Due Date'}")
        print("=" * 60)
        if not active:
            print("No books are currently checked out.")
        for item in active:
            print(f"{item.issue_id:<12} {item.book_id:<10} {item.member_id:<12} {item.due_date}")
        print("=" * 60)

    def print_top_borrowers(self) -> None:
        """Show top 5 members with the highest checkout count."""
        counts = Counter(i.member_id for i in self.issue_mgr.issues).most_common(5)
        print("\n" + "=" * 35)
        print(f"{'Member ID':<15} {'Total Borrows'}")
        print("=" * 35)
        if not counts:
            print("No issue records yet.")
        for member_id, count in counts:
            print(f"{member_id:<15} {count}")
        print("=" * 35)

    def print_fines(self) -> None:
        """Display total revenue from returned book overdue fines."""
        total = sum(i.fine_paid for i in self.issue_mgr.issues)
        print(f"\nTotal Overdue Fines Collected: Rs. {total:.2f}")