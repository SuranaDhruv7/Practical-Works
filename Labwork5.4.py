#1
"""
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): 
     return f"A({self.x}, {self.y})"
o1 = A(3, 4)
print(o1)

#2
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def __len__(self):
        words = self.sentence.split()
        return len(words)

obj1 = Sentence("My name is Dhruv Surana")
print(len(obj1))

#3
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __eq__(self, other):
        if (other, Rectangle):
             self.area == other.area
             return True
        else:
            return False

    def __str__(self):
        return f"Rectangle(length = {self.length}, breadth = {self.breadth}, area = {self.area()})"

length1 = float(input("Enter the length for first rectangle: "))
breadth1 = float(input("Enter the breadth for first rectangle: "))
rect1 = Rectangle(length1, breadth1)

length2 = float(input("Enter the length for second rectangle: "))
breadth2 = float(input("Enter the breadth for second rectangle: "))
rect2 = Rectangle(length2, breadth2)

print(f"Are rect1 and rect2 egual? {rect1 == rect2}")

print(f"Rectangle 1: {rect1}")
print(f"Rectangle 2: {rect2}")

#4
class Box:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

box = Box([10, 20, 30, 40, 50])
print("Items at index 2: ", box[2])

box [2] = 25
print(f"Modified item at index[2]: ", box[2])
print(f"Updated list: ", box.items)

#5
class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(name={self.name!r}, balance={self.balance!r})"

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be Positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

account1 = BankAccount("John Doe", 500.0)
account2 = BankAccount("Jane Smith", 1500.0)

print(account1)
print(account2)

account1.deposit(200)
account1.withdraw(100)

print(account1)

#6
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getData(self):
        print(f"x: {self.x}, y: {self.y}")

    def __add__(self, other):
        ans = self.x + other.x
        ans1 = self.y + other.y
        return Vector(ans, ans1)

o1 = Vector(2, 3)
o1.getData()
o2 = Vector(3, 7)
o2.getData()
result = o1 + o2
result.getData()

#7
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) - (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"

c1 = ComplexNumber(2, 2)
c2 = ComplexNumber(2, 5)
result = c1 * c2
print("Complex number 1:", c1)
print("Complex number 2:", c2)
print("Multiplication result:", result)

#8
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __gt__(self, other):
        time_in_minutes_self = (self.hours * 60) + self.minutes
        time_in_minutes_other = (other.hours * 60) + other.minutes
        return time_in_minutes_self > time_in_minutes_other

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"

time1 = Time(3, 45)
time2 = Time(4, 30)
if time1 > time2:
    print(f"{time1} is greater than {time2}")
else:
    print(f"{time1} is not greater than {time2}")

#9
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __sub__(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return Book (self.title, discounted_price)

    def __str__(self):
        return f"Book: {self.title}, Price: ${self.price:.2f}"

book1 = Book("Python Programming", 100.00)
discounted_book = book1 - 10

print(book1)
print(discounted_book)

#10
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = Matrix(matrix_data)
row_2 = matrix[1]

print("Matrix:")
print(matrix)

print("Accessed Row 2:")
print(row_2)
"""