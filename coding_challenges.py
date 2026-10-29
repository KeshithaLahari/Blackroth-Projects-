"""Ten practical Python OOP coding challenges matching exact Story 6 names."""

from __future__ import annotations

import math


# 1. Student class
class Student:
    def __init__(self, full_name: str, test_scores: list[float]) -> None:
        self.full_name = full_name
        self.test_scores = test_scores

    def calculate_average(self) -> float:
        return sum(self.test_scores) / len(self.test_scores) if self.test_scores else 0.0

    def display_details(self) -> None:
        print(f"Student: {self.full_name} | Average: {self.calculate_average():.2f}")


# 2. Bank account class
class BankAccount:
    def __init__(self, holder_name: str, opening_balance: float = 0.0) -> None:
        self.holder_name = holder_name
        self.balance = opening_balance

    def deposit(self, funds: float) -> None:
        if funds > 0:
            self.balance += funds
            print(f"Deposited: Rs. {funds:.2f}")

    def withdraw(self, funds: float) -> None:
        if 0 < funds <= self.balance:
            self.balance -= funds
            print(f"Withdrawn: Rs. {funds:.2f}")
        else:
            print("Declined: Insufficient funds or invalid amount.")

    def display_balance(self) -> None:
        print(f"Account: {self.holder_name} | Balance: Rs. {self.balance:.2f}")


# 3. Employee management
class Employee:
    def __init__(self, emp_name: str, staff_code: int, monthly_pay: float) -> None:
        self.emp_name = emp_name
        self.staff_code = staff_code
        self.monthly_pay = monthly_pay

    def calculate_annual_salary(self) -> float:
        return self.monthly_pay * 12

    def display_details(self) -> None:
        print(f"Employee #{self.staff_code}: {self.emp_name} | Annual: Rs. {self.calculate_annual_salary():.2f}")


# 4. Vehicle inheritance
class Vehicle:
    def __init__(self, brand_name: str, model_line: str) -> None:
        self.brand_name = brand_name
        self.model_line = model_line

    def display_details(self) -> None:
        print(f"Make: {self.brand_name} {self.model_line}")


class Car(Vehicle):
    def __init__(self, brand_name: str, model_line: str, door_count: int) -> None:
        super().__init__(brand_name, model_line)
        self.door_count = door_count

    def display_details(self) -> None:
        super().display_details()
        print(f"Doors: {self.door_count}")


class Motorcycle(Vehicle):
    def __init__(self, brand_name: str, model_line: str, displacement_cc: int) -> None:
        super().__init__(brand_name, model_line)
        self.displacement_cc = displacement_cc

    def display_details(self) -> None:
        super().display_details()
        print(f"Engine: {self.displacement_cc} cc")


# 5. Shape area calculator
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must calculate area.")


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, span_x: float, span_y: float) -> None:
        self.span_x = span_x
        self.span_y = span_y

    def area(self) -> float:
        return self.span_x * self.span_y


# 6. Shopping cart
class ShoppingCart:
    def __init__(self) -> None:
        self.cart_items: list[tuple[str, float]] = []

    def add_item(self, product_label: str, unit_price: float) -> None:
        if unit_price >= 0:
            self.cart_items.append((product_label, unit_price))
            print(f"Cart added: {product_label} (Rs. {unit_price:.2f})")

    def calculate_total(self) -> float:
        return sum(cost for _, cost in self.cart_items)

    def display_cart(self) -> None:
        for label, cost in self.cart_items:
            print(f"- {label}: Rs. {cost:.2f}")
        print(f"Total: Rs. {self.calculate_total():.2f}")


# 7. Movie rating system
class Movie:
    def __init__(self, film_title: str) -> None:
        self.film_title = film_title
        self.score_registry: list[float] = []

    def add_rating(self, user_score: float) -> None:
        if 1.0 <= user_score <= 10.0:
            self.score_registry.append(user_score)
        else:
            print("Score out of range (1–10).")

    def average_rating(self) -> float:
        return sum(self.score_registry) / len(self.score_registry) if self.score_registry else 0.0

    def display_details(self) -> None:
        print(f"Movie: {self.film_title} | Score: {self.average_rating():.2f}/10 ({len(self.score_registry)} reviews)")


# 8. Hospital patient records
class Patient:
    def __init__(self, chart_number: int, patient_name: str, medical_condition: str, ward_no: int) -> None:
        self.chart_number = chart_number
        self.patient_name = patient_name
        self.medical_condition = medical_condition
        self.ward_no = ward_no

    def display_record(self) -> None:
        print(f"Chart #{self.chart_number} | {self.patient_name} | Condition: {self.medical_condition} | Ward: {self.ward_no}")


# 9. School result processing
class SchoolResult:
    def __init__(self, scholar_name: str, subject_marks: list[float]) -> None:
        self.scholar_name = scholar_name
        self.subject_marks = subject_marks

    def calculate_total(self) -> float:
        return sum(self.subject_marks)

    def calculate_percentage(self) -> float:
        return self.calculate_total() / len(self.subject_marks) if self.subject_marks else 0.0

    def get_result(self) -> str:
        return "Pass" if self.subject_marks and all(m >= 35.0 for m in self.subject_marks) else "Fail"

    def display_result(self) -> None:
        print(f"Scholar: {self.scholar_name} | Total: {self.calculate_total():.0f} | Grade: {self.calculate_percentage():.2f}% ({self.get_result()})")


# 10. Online course management
class OnlineCourse:
    def __init__(self, course_title: str, instructor_name: str) -> None:
        self.course_title = course_title
        self.instructor_name = instructor_name
        self.roster: list[str] = []

    def enroll_student(self, candidate_name: str) -> None:
        if candidate_name not in self.roster:
            self.roster.append(candidate_name)
            print(f"Enrolled {candidate_name} into {self.course_title}")
        else:
            print(f"{candidate_name} already registered.")

    def display_course(self) -> None:
        print(f"Course: {self.course_title} (Lead: {self.instructor_name}) | Class size: {len(self.roster)}")


# Demonstration
def main() -> None:
    print("=== Challenge 1 ===")
    Student("Pooja", [88.0, 91.0, 76.5]).display_details()

    print("\n=== Challenge 2 ===")
    acc = BankAccount("Pooja", 1200.0)
    acc.deposit(300.0)
    acc.withdraw(150.0)
    acc.display_balance()

    print("\n=== Challenge 3 ===")
    Employee("Kavita", 204, 32000.0).display_details()

    print("\n=== Challenge 4 ===")
    Car("Honda", "City", 4).display_details()
    Motorcycle("KTM", "Duke 390", 373).display_details()

    print("\n=== Challenge 5 ===")
    print(f"Circle Area: {Circle(7.0).area():.2f}")
    print(f"Rectangle Area: {Rectangle(6.0, 8.0).area():.2f}")

    print("\n=== Challenge 6 ===")
    cart = ShoppingCart()
    cart.add_item("Wireless Mouse", 850.0)
    cart.add_item("USB-C Hub", 1450.0)
    cart.display_cart()

    print("\n=== Challenge 7 ===")
    film = Movie("Interstellar")
    film.add_rating(9.5)
    film.add_rating(9.0)
    film.display_details()

    print("\n=== Challenge 8 ===")
    Patient(4021, "Dev", "Asthma", 108).display_record()

    print("\n=== Challenge 9 ===")
    SchoolResult("Pooja", [78.0, 82.0, 90.0]).display_result()
    SchoolResult("Kiran", [65.0, 25.0, 80.0]).display_result()

    print("\n=== Challenge 10 ===")
    portal = OnlineCourse("System Design", "Prof. Verma")
    portal.enroll_student("Pooja")
    portal.enroll_student("Kavita")
    portal.display_course()


if __name__ == "__main__":
    main()