"""Ten practical Python OOP coding challenges ."""

from __future__ import annotations

import math


# ============================================================================
# Challenge 1: Trainee Assessment (Average Calculator)
# Concept: Class, attributes, list processing, average computation
# ============================================================================
class Trainee:
    """Track trainee performance and compute evaluation scores."""

    def __init__(self, full_name: str, module_scores: list[float]) -> None:
        self.full_name: str = full_name
        self.module_scores: list[float] = module_scores

    def compute_average(self) -> float:
        """Return the mean of all module scores."""
        if not self.module_scores:
            return 0.0
        return sum(self.module_scores) / len(self.module_scores)

    def print_summary(self) -> None:
        """Display trainee overview and computed average score."""
        print(f"Trainee Name: {self.full_name}")
        print(f"Module Scores: {self.module_scores}")
        print(f"Overall Average: {self.compute_average():.2f}")


# ============================================================================
# Challenge 2: Digital Wallet (Stateful Transaction Engine)
# Concept: Encapsulation, positive constraints, deposit/withdraw guards
# ============================================================================
class DigitalWallet:
    """Manage a digital prepaid wallet with load and payment actions."""

    def __init__(self, owner_tag: str, credits: float = 0.0) -> None:
        self.owner_tag: str = owner_tag
        self.credits: float = credits

    def top_up(self, amount: float) -> None:
        """Add credits to the wallet."""
        if amount <= 0:
            print("Top-up amount must be positive.")
            return

        self.credits += amount
        print(f"Credits Added: Rs. {amount:.2f}")

    def spend(self, amount: float) -> None:
        """Deduct credits if balance is sufficient."""
        if amount <= 0:
            print("Spend amount must be positive.")
        elif amount > self.credits:
            print("Payment declined: Insufficient funds.")
        else:
            self.credits -= amount
            print(f"Paid: Rs. {amount:.2f}")

    def show_balance(self) -> None:
        """Display the current available credits."""
        print(f"Wallet Owner: {self.owner_tag}")
        print(f"Remaining Credits: Rs. {self.credits:.2f}")


# ============================================================================
# Challenge 3: Consultant Retainer (Annual Earnings Calculation)
# Concept: Attributes, annualization calculation, formatted details
# ============================================================================
class Consultant:
    """Track consultant details and project annual billable earnings."""

    def __init__(self, full_name: str, contract_code: int, monthly_retainer: float) -> None:
        self.full_name: str = full_name
        self.contract_code: int = contract_code
        self.monthly_retainer: float = monthly_retainer

    def total_annual_earnings(self) -> float:
        """Calculate total retainer income for 12 months."""
        return self.monthly_retainer * 12

    def display_contract(self) -> None:
        """Display consultant contract summary."""
        print(f"Consultant: {self.full_name}")
        print(f"Contract Code: {self.contract_code}")
        print(f"Monthly Retainer: Rs. {self.monthly_retainer:.2f}")
        print(f"Annual Earnings: Rs. {self.total_annual_earnings():.2f}")


# ============================================================================
# Challenge 4: Watercraft Inheritance Hierarchy
# Concept: Inheritance, super() constructor calls, specialization
# ============================================================================
class Watercraft:
    """Base class for water vessels."""

    def __init__(self, manufacturer: str, vessel_code: str) -> None:
        self.manufacturer: str = manufacturer
        self.vessel_code: str = vessel_code

    def print_specs(self) -> None:
        """Display base vessel specifications."""
        print(f"Shipyard: {self.manufacturer}")
        print(f"Vessel Code: {self.vessel_code}")


class CargoShip(Watercraft):
    """Subclass representing a commercial container ship."""

    def __init__(self, manufacturer: str, vessel_code: str, container_capacity: int) -> None:
        super().__init__(manufacturer, vessel_code)
        self.container_capacity: int = container_capacity

    def print_specs(self) -> None:
        """Display cargo ship specifications."""
        super().print_specs()
        print(f"Container Capacity: {self.container_capacity} TEU")


class Speedboat(Watercraft):
    """Subclass representing a motorized recreational boat."""

    def __init__(self, manufacturer: str, vessel_code: str, horsepower: int) -> None:
        super().__init__(manufacturer, vessel_code)
        self.horsepower: int = horsepower

    def print_specs(self) -> None:
        """Display speedboat specifications."""
        super().print_specs()
        print(f"Engine Rating: {self.horsepower} HP")


# ============================================================================
# Challenge 5: Landscape Region Surface Calculation
# Concept: Polymorphism, abstract base behavior via raise NotImplementedError
# ============================================================================
class LandPlot:
    """Base class for calculating geographical land plots."""

    def calculate_surface(self) -> float:
        """Return the land plot's total area."""
        raise NotImplementedError("Subclasses must implement calculate_surface().")


class CircularPark(LandPlot):
    """Calculate the circular acreage of a public park."""

    def __init__(self, radius_meters: float) -> None:
        self.radius_meters: float = radius_meters

    def calculate_surface(self) -> float:
        """Return area using pi * r^2."""
        return math.pi * (self.radius_meters**2)


class AgriculturalField(LandPlot):
    """Calculate the area of a rectangular field."""

    def __init__(self, length_meters: float, width_meters: float) -> None:
        self.length_meters: float = length_meters
        self.width_meters: float = width_meters

    def calculate_surface(self) -> float:
        """Return area using length * width."""
        return self.length_meters * self.width_meters


# ============================================================================
# Challenge 6: Hardware Procurement Order (Aggregate Calculation)
# Concept: Object state tracking, list of tuples, itemized display
# ============================================================================
class ProcurementOrder:
    """Manage hardware assets and total cost in an order batch."""

    def __init__(self) -> None:
        self.supplies: list[tuple[str, float]] = []

    def log_supply(self, label: str, unit_price: float) -> None:
        """Add an asset line item to the order."""
        if unit_price < 0:
            print("Unit cost cannot be negative.")
            return

        self.supplies.append((label, unit_price))
        print(f"Logged: {label} - Rs. {unit_price:.2f}")

    def compute_subtotal(self) -> float:
        """Calculate total value of all ordered parts."""
        return sum(cost for _, cost in self.supplies)

    def print_manifest(self) -> None:
        """Display an itemized manifest of all supplies."""
        print("\nOrder Manifest:")
        for label, cost in self.supplies:
            print(f"{label}: Rs. {cost:.2f}")
        print(f"Order Subtotal: Rs. {self.compute_subtotal():.2f}")


# ============================================================================
# Challenge 7: Book Review Metric Engine
# Concept: Bound-checked input, numeric rating collection, average metric
# ============================================================================
class BookReviewMetric:
    """Store publication metadata and maintain reader review ratings."""

    def __init__(self, volume_title: str) -> None:
        self.volume_title: str = volume_title
        self.critique_scores: list[float] = []

    def submit_rating(self, score: float) -> None:
        """Accept a score strictly between 1.0 and 10.0."""
        if not 1.0 <= score <= 10.0:
            print("Score must be between 1.0 and 10.0.")
            return

        self.critique_scores.append(score)
        print(f"Recorded review score {score:.1f} for '{self.volume_title}'.")

    def mean_score(self) -> float:
        """Compute the average review score."""
        if not self.critique_scores:
            return 0.0
        return sum(self.critique_scores) / len(self.critique_scores)

    def print_critique_card(self) -> None:
        """Display publication score overview."""
        print(f"Book Title: {self.volume_title}")
        print(f"Total Critiques: {len(self.critique_scores)}")
        print(f"Audience Rating: {self.mean_score():.2f}/10")


# ============================================================================
# Challenge 8: Hotel Reservation Profile
# Concept: Multi-field entity record keeper, formatted card display
# ============================================================================
class HotelReservation:
    """Manage and display guest booking records."""

    def __init__(
        self,
        booking_ref: int,
        guest_name: str,
        room_category: str,
        suite_number: int,
    ) -> None:
        self.booking_ref: int = booking_ref
        self.guest_name: str = guest_name
        self.room_category: str = room_category
        self.suite_number: int = suite_number

    def view_booking_card(self) -> None:
        """Print full reservation particulars."""
        print(f"Reference ID: #{self.booking_ref}")
        print(f"Guest: {self.guest_name}")
        print(f"Category: {self.room_category}")
        print(f"Suite: {self.suite_number}")


# ============================================================================
# Challenge 9: Flight Cadet Flight Test Evaluation
# Concept: Batch score analysis, percentage generation, passing criteria gate
# ============================================================================
class CadetFlightTest:
    """Evaluate pilot cadet drill scores and qualification status."""

    def __init__(self, cadet_alias: str, drill_marks: list[float]) -> None:
        self.cadet_alias: str = cadet_alias
        self.drill_marks: list[float] = drill_marks

    def aggregate_points(self) -> float:
        """Sum total points accumulated."""
        return sum(self.drill_marks)

    def completion_percentage(self) -> float:
        """Compute overall qualification percentage assuming drills out of 100."""
        if not self.drill_marks:
            return 0.0
        return self.aggregate_points() / len(self.drill_marks)

    def assess_certification(self) -> str:
        """Certify Pass if all drills score at least 35 points."""
        if not self.drill_marks:
            return "No drills recorded"
        if all(mark >= 35.0 for mark in self.drill_marks):
            return "Qualified (Pass)"
        return "Disqualified (Fail)"

    def render_dossier(self) -> None:
        """Print assessment scorecard."""
        print(f"Cadet: {self.cadet_alias}")
        print(f"Points Scored: {self.aggregate_points():.0f}")
        print(f"Score Percentage: {self.completion_percentage():.2f}%")
        print(f"Final Outcome: {self.assess_certification()}")


# ============================================================================
# Challenge 10: Masterclass Workshop Directory
# Concept: Member deduplication, roster management, string joining
# ============================================================================
class MasterclassWorkshop:
    """Manage professional masterclass registrations."""

    def __init__(self, workshop_topic: str, lead_mentor: str) -> None:
        self.workshop_topic: str = workshop_topic
        self.lead_mentor: str = lead_mentor
        self.attendees: list[str] = []

    def register_attendee(self, attendee_name: str) -> None:
        """Add attendee if not already on the roster."""
        if attendee_name in self.attendees:
            print(f"Attendee '{attendee_name}' is already on the roster.")
            return

        self.attendees.append(attendee_name)
        print(f"Attendee '{attendee_name}' confirmed.")

    def summarize_workshop(self) -> None:
        """Print workshop roster status."""
        print(f"Topic: {self.workshop_topic}")
        print(f"Mentor: {self.lead_mentor}")
        print(f"Total Confirmed: {len(self.attendees)}")
        print(f"Roster: {', '.join(self.attendees)}")


# ============================================================================
# Demonstration Main
# ============================================================================
def main() -> None:
    """Execute test runs for all 10 challenges."""
    print("=== Challenge 1: Trainee Assessment ===")
    trainee = Trainee("Vikram", [88.0, 92.5, 79.0])
    trainee.print_summary()

    print("\n=== Challenge 2: Digital Wallet ===")
    wallet = DigitalWallet("vikram_pay", 1500.00)
    wallet.top_up(600.00)
    wallet.spend(350.00)
    wallet.show_balance()

    print("\n=== Challenge 3: Consultant Retainer ===")
    advisor = Consultant("Meera", 408, 45000.00)
    advisor.display_contract()

    print("\n=== Challenge 4: Watercraft Inheritance ===")
    cargo = CargoShip("Maersk Marine", "V-901", 18000)
    cargo.print_specs()

    print("\nSpeedboat Details:")
    boat = Speedboat("Yamaha Marine", "SB-22", 300)
    boat.print_specs()

    print("\n=== Challenge 5: Land Plot Surface Area ===")
    park = CircularPark(14.0)
    farm = AgriculturalField(50.0, 30.0)
    print(f"Circular Park Area: {park.calculate_surface():.2f} sq.m")
    print(f"Agricultural Field Area: {farm.calculate_surface():.2f} sq.m")

    print("\n=== Challenge 6: Hardware Procurement Order ===")
    procurement = ProcurementOrder()
    procurement.log_supply("Solid State Drive", 4500.00)
    procurement.log_supply("RAM Module 16GB", 3200.00)
    procurement.log_supply("Cooling Fan Unit", 1100.00)
    procurement.print_manifest()

    print("\n=== Challenge 7: Book Review Metric ===")
    review = BookReviewMetric("Designing Data-Intensive Applications")
    review.submit_rating(9.5)
    review.submit_rating(9.0)
    review.submit_rating(10.0)
    review.print_critique_card()

    print("\n=== Challenge 8: Hotel Reservation Profile ===")
    guest = HotelReservation(7702, "Siddharth", "Executive Suite", 412)
    guest.view_booking_card()

    print("\n=== Challenge 9: Flight Cadet Evaluation (Cadet 1) ===")
    cadet1 = CadetFlightTest("Echo-Leader", [75.0, 80.0, 85.0])
    cadet1.render_dossier()

    print("\n=== Challenge 9: Flight Cadet Evaluation (Cadet 2) ===")
    cadet2 = CadetFlightTest("Bravo-Wing", [90.0, 28.0, 88.0, 70.0])
    cadet2.render_dossier()

    print("\n=== Challenge 10: Masterclass Workshop Directory ===")
    workshop = MasterclassWorkshop("Advanced Architecture & Microservices", "Dr. Rao")
    workshop.register_attendee("Vikram")
    workshop.register_attendee("Meera")
    workshop.register_attendee("Siddharth")
    workshop.summarize_workshop()


if __name__ == "__main__":
    main()