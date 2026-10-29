"""Main entry point for the Library Management System CLI."""

import os
import sys

# Automatically add the root OOP_Project folder to Python's search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from library_management.book import BookManager
from library_management.exceptions import LibraryError
from library_management.issue import IssueManager
from library_management.member import MemberManager
from library_management.reports import ReportService
from library_management.storage import JSONStorage


def main() -> None:
    # Set paths to JSON storage
    data_dir = os.path.join(current_dir, "data")
    storage = JSONStorage()

    books_path = os.path.join(data_dir, "books.json")
    members_path = os.path.join(data_dir, "members.json")
    issues_path = os.path.join(data_dir, "issues.json")

    # Initialize managers
    book_mgr = BookManager(storage, books_path)
    member_mgr = MemberManager(storage, members_path)
    issue_mgr = IssueManager(storage, issues_path, book_mgr, member_mgr)
    reports = ReportService(book_mgr, member_mgr, issue_mgr)

    menu = """
=================================
    LIBRARY MANAGEMENT SYSTEM    
=================================
1. Add New Book
2. Search Books
3. List All Books (Inventory)
4. Register New Member
5. Issue a Book
6. Return a Book
7. View Borrowed Books
8. View Top Borrowers
9. View Fine Report
0. Exit
=================================
"""

    while True:
        print(menu)
        choice = input("Enter choice (0-9): ").strip()

        try:
            if choice == "1":
                title = input("Book Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                copies = int(input("Total Copies: "))
                new_book = book_mgr.add_book(title, author, isbn, copies)
                print(f"[Success] Added '{new_book.title}' with ID: {new_book.book_id}")

            elif choice == "2":
                query = input("Search by title, author, or ISBN: ")
                matches = book_mgr.search(query)
                print(f"\nFound {len(matches)} match(es):")
                for b in matches:
                    print(f"- [{b.book_id}] {b.title} by {b.author} (Available: {b.available_copies}/{b.total_copies})")

            elif choice == "3":
                reports.print_inventory()

            elif choice == "4":
                name = input("Member Name: ")
                email = input("Email: ")
                phone = input("Phone (10 digits): ")
                new_member = member_mgr.register_member(name, email, phone)
                print(f"[Success] Registered '{new_member.name}' with ID: {new_member.member_id}")

            elif choice == "5":
                book_id = input("Book ID (e.g. B001): ")
                member_id = input("Member ID (e.g. M001): ")
                record = issue_mgr.issue_book(book_id, member_id)
                print(f"[Success] Issued! Loan ID: {record.issue_id}. Return by: {record.due_date}")

            elif choice == "6":
                issue_id = input("Issue ID (e.g. ISSUE0001): ")
                record, fine = issue_mgr.return_book(issue_id)
                print("[Success] Book returned.")
                if fine > 0:
                    print(f"[Notice] Overdue fine to collect: Rs. {fine:.2f}")

            elif choice == "7":
                reports.print_borrowed_books()

            elif choice == "8":
                reports.print_top_borrowers()

            elif choice == "9":
                reports.print_fines()

            elif choice == "0":
                print("Exiting application. Goodbye!")
                sys.exit(0)

            else:
                print("[Error] Invalid choice, please enter 0 through 9.")

        except LibraryError as err:
            print(f"[System Error] {err}")
        except ValueError as err:
            print(f"[Input Error] Please enter a valid number: {err}")
        except Exception as err:
            print(f"[Unexpected Error] {err}")


if __name__ == "__main__":
    main()