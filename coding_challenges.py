"""Ten practical Python OOP coding challenges with fresh, real-world examples."""

import math


# ============================================================
# Challenge 1: Cricket Player Batting Tracker
# Concept: Class with attributes and average calculation
# ============================================================

class CricketPlayer:
    """Store player stats and calculate their batting average."""

    def __init__(self, name: str, scores: list[float]) -> None:
        self.name = name
        self.scores = scores

    def calculate_average(self) -> float:
        """Return the average runs scored by the player."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def display_details(self) -> None:
        """Display player name, scores, and average."""
        print(f"Player Name: {self.name}")
        print(f"Recent Scores: {self.scores}")
        print(f"Batting Average: {self.calculate_average():.2f}")


# ============================================================
# Challenge 2: Mobile Recharge Wallet
# Concept: Protected/monitored balance with deposit and deduction checks
# ============================================================

class MobileWallet:
    """Manage a digital cash wallet with add-money and spend operations."""

    def __init__(self, user_name: str, balance: float = 0.0) -> None:
        self.user_name = user_name
        self.balance = balance

    def add_funds(self, amount: float) -> None:
        """Add money to the wallet balance."""
        if amount <= 0:
            print("Recharge amount must be positive.")
            return

        self.balance += amount
        print(f"Recharged: Rs. {amount:.2f}")

    def spend(self, amount: float) -> None:
        """Deduct money if sufficient balance is available."""
        if amount <= 0:
            print("Payment amount must be positive.")
        elif amount > self.balance:
            print("Insufficient wallet balance.")
        else:
            self.balance -= amount
            print(f"Paid: Rs. {amount:.2f}")

    def display_balance(self) -> None:
        """Display the current wallet balance."""
        print(f"Wallet User: {self.user_name}")
        print(f"Available Balance: Rs. {self.balance:.2f}")


# ============================================================
# Challenge 3: Freelance Consultant
# Concept: Store profile details and calculate total yearly fee
# ============================================================

class Consultant:
    """Store consultant details and calculate annual retained income."""

    def __init__(
        self, name: str, consultant_id: int, monthly_retainer: float
    ) -> None:
        self.name = name
        self.consultant_id = consultant_id
        self.monthly_retainer = monthly_retainer

    def calculate_annual_income(self) -> float:
        """Calculate total annual consulting fees."""
        return self.monthly_retainer * 12

    def display_details(self) -> None:
        """Display consultant details and earnings."""
        print(f"Consultant Name: {self.name}")
        print(f"ID Number: {self.consultant_id}")
        print(f"Monthly Retainer: Rs. {self.monthly_retainer:.2f}")
        print(f"Annual Income: Rs. {self.calculate_annual_income():.2f}")


# ============================================================
# Challenge 4: Electronic Gadget Hierarchy
# Concept: Base class inheritance with specialized child classes and super()
# ============================================================

class ElectronicDevice:
    """Represent a general electronic device."""

    def __init__(self, brand: str, model_name: str) -> None:
        self.brand = brand
        self.model_name = model_name

    def display_details(self) -> None:
        """Display general device specs."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model_name}")


class Laptop(ElectronicDevice):
    """Represent a laptop inherited from ElectronicDevice."""

    def __init__(
        self, brand: str, model_name: str, ram_gb: int
    ) -> None:
        super().__init__(brand, model_name)
        self.ram_gb = ram_gb

    def display_details(self) -> None:
        """Display laptop specifications."""
        super().display_details()
        print(f"RAM Capacity: {self.ram_gb} GB")


class SmartWatch(ElectronicDevice):
    """Represent a smartwatch inherited from ElectronicDevice."""

    def __init__(
        self, brand: str, model_name: str, battery_hours: int
    ) -> None:
        super().__init__(brand, model_name)
        self.battery_hours = battery_hours

    def display_details(self) -> None:
        """Display smartwatch battery endurance."""
        super().display_details()
        print(f"Battery Life: {self.battery_hours} hours")


# ============================================================
# Challenge 5: Garden Bed Area Calculator
# Concept: Base abstract shape pattern with polymorphic calculations
# ============================================================

class LandPlot:
    """Base class for agricultural and garden land plots."""

    def area(self) -> float:
        """Calculate and return surface area."""
        raise NotImplementedError("Subclasses must implement area().")


class CircularPond(LandPlot):
    """Calculate the area of a circular pond."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class VegetableBed(LandPlot):
    """Calculate the area of a rectangular vegetable patch."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# ============================================================
# Challenge 6: Food Delivery Order Tray
# Concept: List of item tuples, price validation, and sum accumulation
# ============================================================

class FoodOrder:
    """Manage food dishes and calculate the total restaurant bill."""

    def __init__(self) -> None:
        self.dishes: list[tuple[str, float]] = []

    def add_dish(self, dish_name: str, price: float) -> None:
        """Add a menu item to the meal tray."""
        if price < 0:
            print("Price cannot be negative.")
            return

        self.dishes.append((dish_name, price))
        print(f"Added to tray: {dish_name} - Rs. {price:.2f}")

    def calculate_total(self) -> float:
        """Calculate the total price of all dishes."""
        return sum(price for _, price in self.dishes)

    def display_order(self) -> None:
        """Display the complete food receipt."""
        print("\nOrder Summary:")
        for name, price in self.dishes:
            print(f"- {name}: Rs. {price:.2f}")

        print(f"Grand Total: Rs. {self.calculate_total():.2f}")


# ============================================================
# Challenge 7: Restaurant Customer Review Box
# Concept: Numeric list validation (1 to 10) and average rating
# ============================================================

class Restaurant:
    """Store dining ratings and calculate customer satisfaction."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.reviews: list[float] = []

    def add_review(self, score: float) -> None:
        """Submit a rating between 1 and 10."""
        if not 1 <= score <= 10:
            print("Rating must be between 1 and 10.")
            return

        self.reviews.append(score)
        print(f"Review {score:.1f}/10 submitted for {self.name}.")

    def average_score(self) -> float:
        """Calculate average customer rating."""
        if not self.reviews:
            return 0.0
        return sum(self.reviews) / len(self.reviews)

    def display_details(self) -> None:
        """Display restaurant feedback score."""
        print(f"Restaurant: {self.name}")
        print(f"Total Feedback Given: {len(self.reviews)}")
        print(f"Average Rating: {self.average_score():.2f}/10")


# ============================================================
# Challenge 8: Hotel Guest Booking Record
# Concept: Record storage and formatted card/slip printing
# ============================================================

class HotelGuest:
    """Store and display hotel guest reservation records."""

    def __init__(
        self,
        booking_id: int,
        guest_name: str,
        room_type: str,
        nights: int,
    ) -> None:
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.room_type = room_type
        self.nights = nights

    def display_booking(self) -> None:
        """Display the reservation confirmation."""
        print(f"Booking ID: {self.booking_id}")
        print(f"Guest Name: {self.guest_name}")
        print(f"Room Category: {self.room_type}")
        print(f"Duration: {self.nights} night(s)")


# ============================================================
# Challenge 9: Driver Fitness / Fitness Test Evaluation
# Concept: List filtering, threshold checking (min 35), and Pass/Fail logic
# ============================================================

class DrivingFitnessTest:
    """Calculate and display fitness clearance based on fitness checks."""

    def __init__(self, candidate_name: str, scores: list[float]) -> None:
        self.candidate_name = candidate_name
        self.scores = scores

    def calculate_total_score(self) -> float:
        """Calculate total points across all checkpoints."""
        return sum(self.scores)

    def calculate_percentage(self) -> float:
        """Calculate average points percentage."""
        if not self.scores:
            return 0.0
        return self.calculate_total_score() / len(self.scores)

    def get_clearance_status(self) -> str:
        """Return Pass if every module score is at least 35 points."""
        if not self.scores:
            return "No test scores available"
        if all(score >= 35 for score in self.scores):
            return "Pass"
        return "Fail"

    def display_report(self) -> None:
        """Display the candidate's fitness evaluation."""
        print(f"Candidate: {self.candidate_name}")
        print(f"Total Score: {self.calculate_total_score():.0f}")
        print(f"Performance: {self.calculate_percentage():.2f}%")
        print(f"Status: {self.get_clearance_status()}")


# ============================================================
# Challenge 10: Fitness Club Membership Roster
# Concept: Roster management with duplicate checking and member display
# ============================================================

class FitnessClub:
    """Manage a gym facility and registered athletic members."""

    def __init__(self, club_name: str, head_trainer: str) -> None:
        self.club_name = club_name
        self.head_trainer = head_trainer
        self.members: list[str] = []

    def register_member(self, member_name: str) -> None:
        """Register a new member if not already joined."""
        if member_name in self.members:
            print(f"{member_name} already holds an active membership.")
            return

        self.members.append(member_name)
        print(f"{member_name} registered successfully.")

    def display_club(self) -> None:
        """Display gym details and all enrolled members."""
        print(f"Gym: {self.club_name}")
        print(f"Head Trainer: {self.head_trainer}")
        print(f"Total Active Members: {len(self.members)}")
        print(f"Member List: {', '.join(self.members)}")


# ============================================================
# Full Execution Runner (All 10 Challenges Tested)
# ============================================================

def main() -> None:
    """Demonstrate all 10 unique OOP coding challenges."""

    print("=== Challenge 1: Cricket Player Stats ===")
    batter = CricketPlayer("Rohit", [45.0, 88.0, 102.0])
    batter.display_details()

    print("\n=== Challenge 2: Mobile Wallet ===")
    wallet = MobileWallet("Sunita", 800.00)
    wallet.add_funds(400.00)
    wallet.spend(250.00)
    wallet.display_balance()

    print("\n=== Challenge 3: Freelance Consultant ===")
    advisor = Consultant("Meera", 401, 45000.00)
    advisor.display_details()

    print("\n=== Challenge 4: Electronic Gadget Hierarchy ===")
    laptop = Laptop("Dell", "XPS 15", 16)
    laptop.display_details()

    print("\nSmartwatch Details:")
    watch = SmartWatch("Noise", "ColorFit", 48)
    watch.display_details()

    print("\n=== Challenge 5: Garden Bed Area Calculator ===")
    pond = CircularPond(4.0)
    bed = VegetableBed(6.0, 3.0)
    print(f"Circular Pond Area: {pond.area():.2f} sq meters")
    print(f"Vegetable Bed Area: {bed.area():.2f} sq meters")

    print("\n=== Challenge 6: Food Delivery Order Tray ===")
    order = FoodOrder()
    order.add_dish("Paneer Tikka", 220.00)
    order.add_dish("Butter Naan", 45.00)
    order.add_dish("Mango Lassi", 80.00)
    order.display_order()

    print("\n=== Challenge 7: Restaurant Review Box ===")
    bistro = Restaurant("Spice Route")
    bistro.add_review(9.0)
    bistro.add_review(8.5)
    bistro.add_review(9.5)
    bistro.display_details()

    print("\n=== Challenge 8: Hotel Booking Record ===")
    guest = HotelGuest(2042, "Arjun", "Deluxe Suite", 3)
    guest.display_booking()

    print("\n=== Challenge 9: Driver Fitness Test ===")
    fit_candidate = DrivingFitnessTest("Sunil", [75, 80, 65, 85])
    fit_candidate.display_report()

    print("\nSecond Candidate Evaluation:")
    unfit_candidate = DrivingFitnessTest("Kavita", [70, 30, 85, 90])  # One test < 35
    unfit_candidate.display_report()

    print("\n=== Challenge 10: Fitness Club Membership ===")
    gym = FitnessClub("Iron Pulse Fitness", "Trainer Rajesh")
    gym.register_member("Sunil")
    gym.register_member("Meera")
    gym.register_member("Sunil")  # Duplicate check
    gym.register_member("Deepak")
    gym.display_club()


if __name__ == "__main__":
    main()