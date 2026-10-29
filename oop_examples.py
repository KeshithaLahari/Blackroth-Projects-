# 1. Encapsulation: Keeping things safe inside
class PiggyBank:
    def __init__(self, owner, money):
        self.owner = owner
        self.__money = money  # two underscores keep money hidden and safe

    def see_balance(self):
        return self.__money

    def add_money(self, amount):
        if amount > 0:
            self.__money = self.__money + amount
            print(f"Added {amount} rupees")


# 2. Single Inheritance: Child learns from Parent
class Parent:
    def cook(self):
        print("Cooking delicious food")

class Child(Parent):
    def play(self):
        print("Playing cricket")


# 3. Multilevel Inheritance: Passing skills down generations
class Grandpa:
    def tell_story(self):
        print("Telling an old story")

class Dad(Grandpa):
    def drive(self):
        print("Driving a car")

class Son(Dad):
    def draw(self):
        print("Drawing a picture")


# 4. Hierarchical Inheritance: One parent, different kids
class Mom:
    def make_tea(self):
        print("Making hot tea")

class SonTwo(Mom):
    def study(self):
        print("Reading books")

class Daughter(Mom):
    def sing(self):
        print("Singing a song")


# 5. Multiple Inheritance: Taking features from two things
class Camera:
    def take_photo(self):
        print("Click! Photo taken")

class MusicPlayer:
    def play_music(self):
        print("Playing a nice song")

class Phone(Camera, MusicPlayer):
    def call(self):
        print("Calling my best friend")


# 6. Polymorphism: Same action name, different sound
class Dog:
    def make_sound(self):
        print("Dog says: Bow Bow")

class Cat:
    def make_sound(self):
        print("Cat says: Meow Meow")


# 7. Method Overloading: Saying hello in different ways
class Greeter:
    def say_hello(self, name, message="Hello"):
        print(f"{message}, {name}!")


# 8. Composition: Parts that cannot live alone
class Heart:
    def beat(self):
        print("Heart is beating")

class Human:
    def __init__(self, name):
        self.name = name
        self.heart = Heart()  # human has a heart inside

    def live(self):
        print(f"{self.name} is happy")
        self.heart.beat()


# 9. Aggregation: Friends joining a group
class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"Students in {self.room_name}:")
        for s in self.students:
            print(s.name)


# Running everything so you can see it work
box = PiggyBank("Raju", 100)
print(box.owner)
print(box.see_balance())
box.add_money(50)
print(box.see_balance())

kid = Child()
kid.cook()
kid.play()

family_boy = Son()
family_boy.tell_story()
family_boy.drive()
family_boy.draw()

s2 = SonTwo()
d = Daughter()
s2.make_tea()
s2.study()
d.make_tea()
d.sing()

my_phone = Phone()
my_phone.take_photo()
my_phone.play_music()
my_phone.call()

dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

greet = Greeter()
greet.say_hello("Kiran")
greet.say_hello("Kiran", "Good Morning")

person = Human("Anjali")
person.live()

st1 = Student("Aarav")
st2 = Student("Priya")
room = Classroom("Class 5")
room.add_student(st1)
room.add_student(st2)
room.show_students()