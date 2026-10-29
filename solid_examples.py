"""Simple and clear examples of the five SOLID principles in Python."""

from abc import ABC, abstractmethod


# ============================================================
# S - Single Responsibility Principle (SRP)
# Rule: One class should have only one main job.
# Example: An order holds the food details; the printer prints the receipt.
# ============================================================

class FoodOrder:
    """Store food order details."""

    def __init__(self, item_name: str, price: float) -> None:
        self.item_name = item_name
        self.price = price


class ReceiptPrinter:
    """Handle printing the food receipt."""

    @staticmethod
    def print_receipt(order: FoodOrder) -> None:
        print(f"Receipt: {order.item_name} - Rs. {order.price:.2f}")


# ============================================================
# O - Open/Closed Principle (OCP)
# Rule: Open to add new features, closed to changing old code.
# Example: Add new discount plans without changing the checkout register.
# ============================================================

class DiscountStrategy(ABC):
    """Blueprint for any discount plan."""

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        """Calculate the final price after discount."""
        raise NotImplementedError


class NormalDiscount(DiscountStrategy):
    """Standard customer discount: Rs. 20 off."""

    def apply_discount(self, total: float) -> float:
        return total - 20.0


class FestivalDiscount(DiscountStrategy):
    """Festival discount: 20% off."""

    def apply_discount(self, total: float) -> float:
        return total * 0.80


class CashCounter:
    """Calculates final bill using any discount given to it."""

    def __init__(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def pay_amount(self, total: float) -> float:
        return self.discount.apply_discount(total)


# ============================================================
# L - Liskov Substitution Principle (LSP)
# Rule: Subclasses must fit where parent classes are used.
# Example: Both Sparrow and Penguin are birds that move in their own way.
# ============================================================

class Bird(ABC):
    """Blueprint for all birds."""

    @abstractmethod
    def move(self) -> str:
        """Every bird has a way to move."""
        raise NotImplementedError


class Sparrow(Bird):
    """A bird that moves by flying."""

    def move(self) -> str:
        return "Sparrow is flying in the sky"


class Penguin(Bird):
    """A bird that moves by swimming."""

    def move(self) -> str:
        return "Penguin is swimming in cold water"


def show_bird_movement(bird: Bird) -> None:
    """Works smoothly with any kind of bird."""
    print(bird.move())


# ============================================================
# I - Interface Segregation Principle (ISP)
# Rule: Don't force a class to use features it does not need.
# Example: An old phone only calls; a smartphone calls and takes photos.
# ============================================================

class CallingFeature(ABC):
    """Blueprint for phone calls."""

    @abstractmethod
    def make_call(self, phone_number: str) -> str:
        raise NotImplementedError


class CameraFeature(ABC):
    """Blueprint for taking pictures."""

    @abstractmethod
    def take_photo(self) -> str:
        raise NotImplementedError


class KeypadPhone(CallingFeature):
    """An old phone that only makes calls."""

    def make_call(self, phone_number: str) -> str:
        return f"Calling {phone_number} from keypad phone"


class ModernSmartPhone(CallingFeature, CameraFeature):
    """A smartphone that can call and take photos."""

    def make_call(self, phone_number: str) -> str:
        return f"Calling {phone_number} from smartphone"

    def take_photo(self) -> str:
        return "Click! High-quality photo saved"


# ============================================================
# D - Dependency Inversion Principle (DIP)
# Rule: Rely on a common blueprint rather than hardcoding tools.
# Example: Send alerts through any messaging tool (Email or SMS).
# ============================================================

class AlertSender(ABC):
    """Blueprint for sending any notification."""

    @abstractmethod
    def send_alert(self, text: str) -> str:
        raise NotImplementedError


class EmailService(AlertSender):
    """Send alert using Email."""

    def send_alert(self, text: str) -> str:
        return f"Email Alert: {text}"


class SMSService(AlertSender):
    """Send alert using SMS text."""

    def send_alert(self, text: str) -> str:
        return f"SMS Alert: {text}"


class NotificationManager:
    """Manages notifications by plugging in any AlertSender."""

    def __init__(self, sender: AlertSender) -> None:
        self.sender = sender

    def broadcast(self, text: str) -> str:
        return self.sender.send_alert(text)


# ============================================================
# Main runner to verify all 5 principles
# ============================================================

def main() -> None:
    """Demonstrate all five SOLID principles with simple examples."""

    print("\n--- S: Single Responsibility Principle ---")
    order = FoodOrder("Paneer Butter Masala", 280.00)
    ReceiptPrinter.print_receipt(order)

    print("\n--- O: Open/Closed Principle ---")
    total_bill = 500.00
    counter = CashCounter(FestivalDiscount())
    print(f"Original Bill: Rs. {total_bill:.2f}")
    print(f"After Festival Discount: Rs. {counter.pay_amount(total_bill):.2f}")

    print("\n--- L: Liskov Substitution Principle ---")
    show_bird_movement(Sparrow())
    show_bird_movement(Penguin())

    print("\n--- I: Interface Segregation Principle ---")
    old_phone = KeypadPhone()
    print(old_phone.make_call("9876543210"))
    smartphone = ModernSmartPhone()
    print(smartphone.make_call("9876543210"))
    print(smartphone.take_photo())

    print("\n--- D: Dependency Inversion Principle ---")
    email_notifier = NotificationManager(EmailService())
    sms_notifier = NotificationManager(SMSService())
    print(email_notifier.broadcast("Your food order is on the way!"))
    print(sms_notifier.broadcast("Delivery driver is at your door!"))

    print("\nAll SOLID principles demonstrated successfully!")


if __name__ == "__main__":
    main()