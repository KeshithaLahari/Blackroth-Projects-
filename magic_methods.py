
# Magic Methods in Python
# Magic methods start and end with double underscores.


# 1. __init__ - Initializes an object
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Lahari")
print(s1.name)


# 2. __str__ - Prints an object in a readable way
class Dog:
    def __str__(self):
        return "I am a dog"

d1 = Dog()
print(d1)


# 3. __len__ - Returns the length
class Bag:
    def __len__(self):
        return 5

b1 = Bag()
print(len(b1))


# 4. __add__ - Uses the + operator
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)


# 5. __eq__ - Compares two objects
class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

f1 = Fruit("Apple")
f2 = Fruit("Apple")
print(f1 == f2)


# 6. __repr__ - Shows an object's representation
class Book:
    def __repr__(self):
        return "A Book Object"

book = Book()
print(repr(book))


# 7. __getitem__ - Gets an item using an index
class Colors:
    def __getitem__(self, index):
        colors = ["Red", "Blue", "Green"]
        return colors[index]

c = Colors()
print(c[0])


# 8. __call__ - Calls an object like a function
class Hello:
    def __call__(self):
        print("Hello!")

h = Hello()
h()


# 9. __del__ - Called when an object is finalized
class Test:
    def __del__(self):
        print("Object finalized")

t = Test()
del t
