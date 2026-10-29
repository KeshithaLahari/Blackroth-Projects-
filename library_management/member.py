"""Member model and manager for registering and managing patrons."""

from library_management.exceptions import MemberNotFoundError
from library_management.storage import JSONStorage
from library_management.validator import check_email, check_phone, check_text


class Member:
    """Represents a library member."""

    def __init__(
        self,
        member_id: str,
        name: str,
        email: str,
        phone: str,
        is_active: bool = True,
    ) -> None:
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = is_active

    def to_dict(self) -> dict:
        """Convert member object to a dictionary for JSON saving."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        """Build a Member object from JSON data."""
        return cls(
            member_id=data["member_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            is_active=data.get("is_active", True),
        )


class MemberManager:
    """Handles adding and looking up library members."""

    def __init__(self, storage: JSONStorage, filepath: str) -> None:
        self.storage = storage
        self.filepath = filepath
        self.members: list[Member] = [
            Member.from_dict(d) for d in self.storage.load(filepath)
        ]

    def _save(self) -> None:
        """Helper to save member list back to JSON."""
        self.storage.save(self.filepath, [m.to_dict() for m in self.members])

    def register_member(self, name: str, email: str, phone: str) -> Member:
        """Add a new member after checking their details."""
        valid_name = check_text(name, "Name")
        valid_email = check_email(email)
        valid_phone = check_phone(phone)

        member_id = f"M{len(self.members) + 1:03d}"
        new_member = Member(member_id, valid_name, valid_email, valid_phone)
        self.members.append(new_member)
        self._save()
        return new_member

    def find_by_id(self, member_id: str) -> Member:
        """Find a member by ID or raise an error if not found."""
        clean_id = member_id.strip().upper()
        for member in self.members:
            if member.member_id == clean_id:
                return member
        raise MemberNotFoundError(f"Member '{member_id}' does not exist.")
        