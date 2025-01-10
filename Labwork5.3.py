#1
"""
class addition:
    def add (self, a):
        print(a + a )

class poly(addition):
    def add (self, a):
        if isinstance(a, int):
            print(a + a)
        else:
            super().add(a)
        
obj = poly()

obj.add(25)
obj.add("POLYMORPHISM")

#2
class shape:
    def __init__(self):
        self.width = None
        self.height = None
    
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        self.width = float(input("Enter the width: "))
        self.height = float(input("Enter the height: "))
        print(f"The area of rectangle is {self.width*self.height}")

class Circle(shape):
    def area(self):
         self.width = float(input("Enter the width of circle: "))
         self.pi = 3.14
         print(f"The area of circle is {self.pi*self.width*self.width}")
        
obj = Rectangle()
obj1 = Circle()
         
obj.area()
obj1.area()

#3
class Many():
    def poly(self):
        string = "fvbdvbbfnmv"
        print("Length of string: ", len(string))

class Any(Many):
    def poly(self):
        lst = ["1, 2, 3, 4, 5, 6"]
        print("Length of list: ", len(lst))

class Nany(Many):
    def poly(self):
       dictionary = {"Name": "Dhruv", "Age": "18"}
       super().poly()
       print("Length of dictionary", len(dictionary))

obj1 = Any()
obj2 = Nany()
obj1.poly()
obj2.poly()

#4
class Transport:
    pass

class Train(Transport):
        def travel(self):
            print("Train runs on railway track!")

class Plane(Transport):
     def travel(self):
          print("Plane will land on correct time!")
obj = Train()
obj1 = Plane()

obj.travel()
obj1.travel()

#5
class Calculator:
    def multiple(self, a, b, c=1):
        result = a*b*c
        print(f"Multiplication result: {result}")

calc = Calculator()

calc.multiple(5, 3)
calc.multiple(5, 3, 2)

class Calculator:
    def multiple(self, *args):
        result = 1
        for num in args:
            result *= num
        print(f"Multiplication result: {result}")
calc = Calculator()

calc.multiple(5, 3)
calc.multiple(5, 3, 2)
calc.multiple(5, 3, 2, 4)

#6
class Animal:
    def __init__(self):
        print("Animal makes a sound.")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

#7
#STATIC METHOD
import math

class Shape:
    @staticmethod
    def area(*args):
        if len(args) == 1:
            radius = args[0]
            return math.pi * (radius ** 2)
        elif len(args) == 2:
            length, width = args
            return length * width
        else:
            raise ValueError("Invalid number of arguments. One argument for circle or two for rectangle.")
radius = 5
circle_area = Shape.area(radius)
print(f"Area of circle with radius {radius}: {circle_area:.2f} square units")
length = 4
width = 6
rectangle_area = Shape.area(length, width)
print(f"Area of rectangle with length {length} and width {width}: {rectangle_area} square units")
#CLASS METHOD
class Shape:
    @classmethod
    def area(cls, *args):
        if len(args) == 1:
            radius = args[0]
            return math.pi * (radius ** 2)
        elif len(args) == 2:
            length, width = args
            return length * width
        else:
            raise ValueError("Invalid number of arguments. One argument for circle or two for rectangle.")
"""

#8
class Vehicle:
    def start(self):
        """Parent class method to start the vehicle"""
        print("The vehicle is starting...")

class Bike(Vehicle):
    def start(self):
        """Overridden method in Bike class"""
        print("The bike is starting with a kick!")

class Car(Vehicle):
    def start(self):
        """Overridden method in Car class"""
        print("The car is starting with the push of a button!")
vehicle = Vehicle()
bike = Bike()
car = Car()
print("Vehicle:")
vehicle.start()

print("\nBike:")
bike.start() 

print("\nCar:")
car.start()

#9
class Printer:
    def print(self, *args):
        """Method to print string, integer or both depending on the arguments."""
        if len(args) == 1:
            if isinstance(args[0], str):
                print(f"String: {args[0]}")
            elif isinstance(args[0], int):
                print(f"Integer: {args[0]}")
        elif len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], int):
                print(f"String: {args[0]} and Integer: {args[1]}")
            elif isinstance(args[0], int) and isinstance(args[1], str):
                print(f"Integer: {args[0]} and String: {args[1]}")
        else:
            print("Invalid number of arguments!")

printer = Printer()
print("Test 1: Print a string")
printer.print("Hello, World!")

print("\nTest 2: Print an integer")
printer.print(123)

print("\nTest 3: Print both a string and an integer")
printer.print("Age", 30)

#10
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")
student1 = Student("John", 20, "S12345")
result = issubclass(Student, Person)
print(f"Is Student a subclass of Person? {result}")

#11
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Manager's Department: {self.department}")
manager = Manager("Alice", 80000, "Sales")
manager.display()

#12
class Grandparent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from the Grandparent class!")
class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} from the Parent class!")
class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def greet(self):
        print(f"Hello, I am {self.name} from the Child class!")
print("Is Child a subclass of Parent?", issubclass(Child, Parent))  # Should be True
print("Is Parent a subclass of Grandparent?", issubclass(Parent, Grandparent))  # Should be True
print("Is Child a subclass of Grandparent?", issubclass(Child, Grandparent))  # Should be True
print("Is Parent a subclass of Child?", issubclass(Parent, Child))  # Should be False

#13
# Base Class
class Base:
    def display(self):
        print("This is the display method from the Base class.")

# Derived Class
class Derived(Base):
    def display(self):
        super().display()  
        print("This is the display method from the Derived class.")
derived_object = Derived()
derived_object.display()

#14
# Base Class - User
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print(f"User created with Username: {self.username} and Password: {self.password}")

# Derived Class - Admin
class Admin(User):
    def __init__(self, username, password, admin_level):
        super().__init__(username, password)
        self.admin_level = admin_level
        print(f"Admin created with Admin Level: {self.admin_level}")
admin_user = Admin("admin123", "admin@123", "Level 1")