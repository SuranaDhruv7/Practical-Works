#1
"""
class Person:
    def __init__(self):
        self.__name = input("Enter your name: ")
        self.__age = input("Enter your age: ")
        self.__date_of_birth = input("Enter your date of birth: ")
        self.__place_of_birth = input("Enter your place of birth: ")

    def getData(self):
        print(self.__name, self.__age, self.__date_of_birth, self.__place_of_birth)
person = Person()
person.getData()
"""

#2
"""
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count +=1
    def display(self):
        print(f"The number is being incremented : {self.count}")
counter = Counter()
counter.increment()
counter.display()
counter.increment()
counter.display()  
counter.increment()
counter.display()
"""

#3
"""
class my_class:
    def __init__(self, name):
        self.name = name
        print(f"Object created for {self .name}")
    def __del__(self):
        print(f"Object for {self .name} is being deleted")
obj1 = my_class("Object 1")
obj2 = my_class("Object 2")
obj3 =  my_class("Object 3")
del obj1
del obj2
del obj3
"""

#4
"""
class Counter:
    def __init__():
        self.count = 0
    def increment():
        self.count +=1
    def display():
        print(f"The number is being incremented : {self.count}")
counter = Counter()
counter.increment()
counter.display()
counter.increment()
counter.display()  
counter.increment()
counter.display()
"""

#5
"""
class Animal:
    def __init__(self, ):
         self.__animal = input("Enter the animal: ")
    def getData(self):
        print(f"The animal name is: {self.__animal}")
animal = Animal()
animal.getData()
animal1 = Animal()
animal1.getData()
"""

#6
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length* self.width
rect = Rectangle(5, 3)
area = rect.calculate_area()
print(f"The area of the rectangle is: {area}")

#7
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        print(f"Employee {self.name} ({self.position}) has been hired!")

    def __del__(self):
        print(f"Goodbye {self.name}! Thank you for your contribution as a {self.position}.")

emp1 = Employee("John Doe", "Software Developer", 70000)
del emp1

#8
class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

book1 = Book("To Kill a Mockingbird", "Harper Lee")

print("Book Title:", book1.get_title())
print("Book Author:", book1.get_author())
book1.set_title("1984")
book1.set_author("George Orwell")
print("\nUpdated Book Title:", book1.get_title())
print("Updated Book Author:", book1.get_author())

#9
class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance is: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. Current balance is: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current balance is: {self.__balance}")
account = Account(1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.display_balance()

#10
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be greater than 0.")

    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}")
try:
    person = Person("John", 25)
    person.display()
    person.set_age(-5)
except ValueError as e:
    print(e)
try:
    person_invalid = Person("Alice", -10)
except ValueError as e:
    print(e)

#11
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def calculate_average(self):
        average = sum(self.__marks) / len(self.__marks)
        return average
    
    def calculate_grade(self):
        average = self.calculate_average()
        
        if average >= 90:
            grade = 'A'
        elif average >= 75:
            grade = 'B'
        elif average >= 50:
            grade = 'C'
        else:
            grade = 'F'
            
        return grade
    def display_student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.__marks}")
        print(f"Average Marks: {self.calculate_average()}")
        print(f"Grade: {self.calculate_grade()}")
student1 = Student("John", [85, 90, 78])
student1.display_student_info()

student2 = Student("Alice", [55, 60, 58])
student2.display_student_info()
"""