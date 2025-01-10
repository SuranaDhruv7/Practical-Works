#1
"""
s={12, 13, 14, 15, 20, 3, 5}
s.add(40)
s.remove(3)
print(s)
print(type(s))
print("Set will not allow dupliacte elements because  Sets are designed to store unique elements only. Each element must be unique based on its equals() method.")

#2
dict1= {'Name ': 'Alice' , 'Age':25, 'City' : 'New york'}
dict1['Country'] = 'USA'
dict1['Name '] = 'Dhruv'
del dict1['City']
print(dict1)

#3
list1 = []
s1=int(input("Enter your number: "))
for i in range(s1):
    s2=int(input("Enter the values: "))
    list1.append(s2)
s3 = set(list1)
s4 = list(s3)
print(s4)

#4
product={}
a1 = int(input("ENTER THE NUMBERS :-- "))
for i in range(a1):
    product_name = input("Enter the product name:-- ")
    product_price = float(input("Enter the product price :-- "))
    product[product_name]=product_price
highest_price=max(product.values())

for name in product:
    if product[name] == highest_price:
        highest_product = name
print(f"\nThe product with the highest price is {highest_product}, {highest_price}")
#5
str = input("Enter string: ")
char_frequency = {}
for char in str:
    if char in char_frequency:
        char_frequency[char] += 1

    else:
        char_frequency[char] = 1
print("\nCharacter frequencies:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")

#6
# This is a single-line comment explaining the purpose of the script
# This script calculates the area of a circle and displays the result.

import math
def calculate_area(radius):
    #This is a multi-line comment (docstring) that explains the purpose
    of the function 'calculate_area'. It takes the radius of the circle as
    input and returns the calculated area using the formula: area = pi * r^2.
    area = math.pi * radius ** 2
    return area
radius = 5  
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")  # Inline comment explaining the print statement

#7
def factorial(n):
    # If n is 0 or 1, the factorial is 1 (base case)
    if n == 0 or n == 1:
        return 1
    else:
        # Otherwise, calculate factorial recursively by calling the function
        return n * factorial(n - 1)

# Input: Ask the user to enter a number
num = int(input("Enter a number to calculate its factorial: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and display the result
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
"""

#8
# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    """
    This function calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle, calculated as length * width.
    """
    # Calculate the area by multiplying length and width
    area = length * width
    return area

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function to calculate the area
area = calculate_rectangle_area(length, width)

# Display the result
print(f"The area of the rectangle is: {area}")

#9
"""
# Original list
original_list = [1, 2, 3, 4, 5, 2, 3]
print("Original List:", original_list)

# Convert the list into a set (removes duplicates)
converted_set = set(original_list)
print("\nConverted Set:", converted_set)

# Convert the list into a tuple
converted_tuple_from_list = tuple(original_list)
print("\nConverted Tuple from List:", converted_tuple_from_list)

# Convert a tuple into a list
original_tuple = (1, 2, 3, 4, 5)
converted_list_from_tuple = list(original_tuple)
print("\nConverted List from Tuple:", converted_list_from_tuple)

# Convert a set into a list
original_set = {1, 2, 3, 4, 5}
converted_list_from_set = list(original_set)
print("\nConverted List from Set:", converted_list_from_set)

# Convert a set into a tuple
converted_tuple_from_set = tuple(original_set)
print("\nConverted Tuple from Set:", converted_tuple_from_set)
#10
# Function to take input, convert, and display results
def convert_and_display():
    # Take input from the user (comma-separated numbers)
    input_string = input("Enter a string of comma-separated numbers: ")

    # Split the input string into a list of numbers (strings)
    input_list = input_string.split(",")
    
    # Convert the list to a set (removes duplicates)
    input_set = set(input_list)
    
    # Convert the list to a tuple
    input_tuple = tuple(input_list)
    
    # Display the converted results
    print("\nConverted List:", input_list)
    print("Converted Set:", input_set)
    print("Converted Tuple:", input_tuple)

# Call the function
convert_and_display()

#11
def convert_and_display():
    input_dict = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2, 'c': 3}): "))
    
    keys_list = list(input_dict.keys())
    
    keys_set = set(input_dict.keys())
    
    values_list = list(input_dict.values())
    
    values_tuple = tuple(input_dict.values())
    
    print("\nConverted Keys (List):", keys_list)
    print("Converted Keys (Set):", keys_set)
    print("Converted Values (List):", values_list)
    print("Converted Values (Tuple):", values_tuple)
convert_and_display()

#12
def remove_duplicates_and_retain_order():
    original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
    
    print("Original List with Duplicates:", original_list)
    
    unique_set = set(original_list)
    print("Set after removing duplicates:", unique_set)
 
    order_preserved_list = []
    for item in original_list:
        if item not in order_preserved_list:
            order_preserved_list.append(item)
    
    print("List after removing duplicates and preserving order:", order_preserved_list)

remove_duplicates_and_retain_order()
"""

#13
def set_to_dict_with_square_values():
    unique_integers = {1, 2, 3, 4, 5, 6}
    
    print("Set of unique integers:", unique_integers)
    

    square_dict = {num: num ** 2 for num in unique_integers}
    
    print("Dictionary with integers as keys and their squares as values:", square_dict)

set_to_dict_with_square_values()
