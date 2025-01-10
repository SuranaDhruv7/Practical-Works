#1
"""
class Parent:
    def disp(self):
        print("From class Parent.")

class Child(Parent):
    def child(self):
        print("From class Child.")

obj = Child()

obj.child()
obj.disp()
#2
class Headmaster:
    def __init__(self):
        self.school = None

class Teacher(Headmaster):
    def getschoolrecord(self):
        self.school = "Books"
        print(self.school)

class Administrator(Headmaster):
    def getschoolrecord(self):
        self.school = "Students"
        print(self.school)

o1 = Teacher() 
o2 = Administrator()

o1.getschoolrecord()
o2.getschoolrecord()

#3
class Grandparent:
    def disp(self):
        print("I am your Granparent")

class Parent(Grandparent):
    def show(self):
        print("I am your Parent")

class Child(Parent):
    def child(self):
        print("I am the Child")

obj = Child()

obj.show()
obj.disp()
obj.child()

#4
class Animal:
    def __init__(self):
        self.breed = input("Enter the breed: ")
        self.colour = input("Enter the colour: ")
        print(f"The breed of the animal is {self.breed} and colour is {self.colour}")

class Dog(Animal):
    def getdata(self):
        print("I am the Dog")

class Cat(Animal):
    def getset(self):
        print("I am the Cat")

abc = Dog()
abc.getdata()
obj = Cat()
obj.getset()

#5
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Bird:
    def __init__(self, species):
        self.species = species
    
    def fly(self):
        print(f"{self.species} can fly.")

class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def speak(self):
        super().speak()
        print(f"{self.name} says: {self.sound}")

class Bat(Mammal, Bird):
    def __init__(self, name, sound, species):
        Mammal.__init__(self, name, sound)
        Bird.__init__(self, species)
    
    def display_info(self):
        print(f"{self.name} is a {self.species}.")
        print(f"It says: {self.sound}")
        self.speak()
        self.fly()

bat = Bat("Batman", "Screech", "Fruit Bat")
bat.display_info()

#6
a = int(input("Enter the number: "))
b = input("Enter the name: ")
print(type(a))
print(type(b))

#7
a = 10
b = 10
if id(a) == id(b):
    print(f"The variables 'a' and 'b' refer to the same memory location: {id(a)}")
else:
    print(f"The variables 'a' and 'b' refer to different memory locations. 'a': {id(a)}, 'b': {id(b)}")

b = 20
if id(a) == id(b):
    print(f"After modification, the variables 'a' and 'b' refer to the same memory location: {id(a)}")
else:
    print(f"After modification, the variables 'a' and 'b' refer to different memory locations. 'a': {id(a)}, 'b': {id(b)}")

#8
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

    def update_position(self, new_position):
        self.position = new_position
employee = Employee("John Doe", 30, "Software Engineer")
attributes_methods = dir(employee)
print("Attributes and Methods of the Employee class:")
for item in attributes_methods:
    print(item)

#9
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."
animal_obj = Animal("Elephant")
dog_obj = Dog("Buddy")
print(isinstance(animal_obj, Animal))
print(isinstance(dog_obj, Animal))     
print(isinstance(dog_obj, Dog))
print(isinstance(animal_obj, Dog))     

#10
class Rectangle:

    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

def multiply(x, y):
    return x * y
print("Help on Rectangle class:")
help(Rectangle)
print("\nHelp on multiply function:")
help(multiply)

#11
def calculate_square_and_cube(number):
    def calculate_cube(n):
        return n ** 3
    square = number ** 2
    cube = calculate_cube(number)
    
    return square, cube
num = 4
square, cube = calculate_square_and_cube(num)

print(f"The square of {num} is {square}.")
print(f"The cube of {num} is {cube}.")

#12
def calculate_string_length(input_string):
    
    def print_length(string):
        print(f"The length of the string '{string}' is: {len(string)}")
        print_length(input_string)
input_str = "Hello, World!"
calculate_string_length(input_str)

#13
def calculate_string_length(input_string):
    
    def print_length(string):
        print(f"The length of the string '{string}' is: {len(string)}")
        print_length(input_string)
input_str = "Hello, World!"
calculate_string_length(input_str)
"""