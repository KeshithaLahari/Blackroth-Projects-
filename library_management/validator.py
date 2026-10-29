"""Simple input checks for the library system."""

from library_management.exceptions import ValidationError


def check_text(value: str, field_name: str) -> str:
    """Make sure a field is not blank."""
    clean = value.strip()
    if not clean:
        raise ValidationError(f"{field_name} cannot be empty.")
    return clean


def check_positive_number(value: int, field_name: str) -> int:
    """Make sure a number is 1 or more."""
    if value <= 0:
        raise ValidationError(f"{field_name} must be greater than 0.")
    return value


def check_phone(phone: str) -> str:
    """Make sure phone is exactly 10 digits."""
    clean = phone.strip()
    if len(clean) != 10 or not clean.isdigit():
        raise ValidationError("Phone number must have exactly 10 digits.")
    return clean


def check_email(email: str) -> str:
    """Simple check for an '@' and a '.' in email."""
    clean = email.strip()
    if "@" not in clean or "." not in clean:
        raise ValidationError("Please enter a valid email address.")
    return clean