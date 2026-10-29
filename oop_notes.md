# Python OOP Fundamentals

## 1. What is OOP?

Object-Oriented Programming (OOP) is a programming approach that organizes code using classes and objects.

OOP helps us create reusable, maintainable, and modular applications.

Real-world example: A library has books. Each book has a title, author, and availability status.

## 2. Classes and Objects

A class is a blueprint. An object is an instance of a class.

python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basics", "Ravi")

print(book1.title)
print(book1.author)


Output:
text
Python Basics
Ravi


## 3. Constructor: _init_()

The _init_() method initializes an object's attributes when an object is created.

python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Anand", 90)
print(student1.name)
print(student1.marks)


## 4. Instance and Class Variables

Instance variables belong to individual objects.

Class variables are shared through the class and normally accessed using the class name.

python
class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name

e1 = Employee("Anand")
e2 = Employee("Ravi")

print(e1.name)
print(e2.name)
print(Employee.company)


## 5. Instance, Class and Static Methods

- Instance methods use self and work with object-specific data.
- Class methods use cls and work with class-level data.
- Static methods do not automatically receive self or cls.

python
class Calculator:
    def add(self, a, b):
        return a + b

    @classmethod
    def description(cls):
        return "Calculator class"

    @staticmethod
    def multiply(a, b):
        return a * b

calc = Calculator()

print(calc.add(2, 3))
print(Calculator.description())
print(Calculator.multiply(2, 3))


Output:
text
5
Calculator class
6


## 6. Understanding self and cls

- self refers to the current object.
- cls refers to the class itself.
- Python passes self to an instance method automatically.
- Python passes cls to a class method automatically.

## 7. Object Lifecycle

1. Create an object by calling its class.
2. Python allocates and initializes the object.
3. Use the object to access attributes and methods.
4. When the object is no longer referenced, it may eventually be garbage-collected.

## 8. Real-World Example

In a library application:

- Book is a class.
- A particular book is an object.
- title and author are attributes.
- display_details() is a method.
- _init_() initializes the book.

## 9. Important Comparisons

| Concept | Meaning |
|---|---|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Instance variable | Data belonging to an object |
| Class variable | Data associated with the class |
| Instance method | Operates on an object |
| Class method | Operates on class-level data |
| Static method | Utility operation related to the class |