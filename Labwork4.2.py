#1
"""
def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact (n-1)
a = int(input("Enter the number: "))
print(fact(a))
"""

#2
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
test_values = [0, 1, 2, 3, 4, 5, 6, 7]
results = {n: fibonacci(n) for n in test_values}
print(results)
"""

#3
"""
def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
input_string = str(input("Enter the string to reverse : "))
print(f"The reversed string is: , {reverse_string(input_string)}")

#4

def digital_root(n):
    if n < 10:
        return n
    else:
        digit_sum = sum(int(digit) for digit in str(n))
        return digital_root(digit_sum)
print("digital_root(400)")
print("")

#5
def is_prime(num, divisor=2):
    if num < 2:
        return False  
    if divisor * divisor > num:
        return True
    
    if num % divisor == 0:
        return False
    
    return is_prime(num, divisor + 1)

def print_primes(start, end):
   
    if start > end:
        return 
    
    if is_prime(start):
        print(start, end=' ')
    
    print_primes(start + 1, end)
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print(f"Prime numbers between {start} and {end} are:")
print_primes(start, end)

#6
numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print("Squared numbers:", squared_numbers)

#7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#8
largest = lambda a, b, c: max(a, b, c)
num1 = 10
num2 = 25
num3 = 15
result = largest(num1, num2, num3)
print("The largest number is:", result)
"""

#9
"""
num = 0
def hero():
    global num
    num = num + 1
    print("Functions called!")
a = int(input("Enter the number: "))
for i in range(a):
    hero()
print(num)
"""

#10
"""
num = 0
def bull(*args):
    global num
    for i in args:
        num = num + 1
        print(num)
bull(1, 2, 3, 4, 5)

#11
username = "Guest"

def update_username(new_name):
    global username
    username = new_name
print("Current username:", username)
new_name = input("Enter a new username: ")
update_username(new_name)
print("Updated username:", username)

#12
global_value = 0
def initialize_value(value):
    global global_value  
    global_value = value
def increment_value(increment):
    global global_value
    global_value += increment
initialize_value(10)
print("Initialized value:", global_value)
increment_amount = int(input("Enter a value to increment by: "))
increment_value(increment_amount)
print("Updated value after increment:", global_value)

#13
variable = "I am a global variable"

def demonstrate_local_vs_global():
    variable = "I am a local variable"
    
    print("Inside the function:")
    print("Local variable:", variable)
print("Outside the function:")
print("Global variable:", variable)
demonstrate_local_vs_global()
print("\nAfter function call:")
print("Global variable:", variable) 
"""

#14
def calculate_sum_max_min(numbers):
    """
    This function takes a list of integers and returns the sum, maximum, and minimum values.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    tuple: A tuple containing the sum, maximum, and minimum values in that order.
    """
    total_sum = sum(numbers)
    maximum_value = max(numbers)
    minimum_value = min(numbers)
    
    return total_sum, maximum_value, minimum_value
numbers_list = [10, 20, 30, 40, 50]
sum_value, max_value, min_value = calculate_sum_max_min(numbers_list)
print("Sum:", sum_value)
print("Maximum:", max_value)
print("Minimum:", min_value)

#15
def calculate_area_and_perimeter(length, width):
    """
    This function calculates the area and perimeter of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    tuple: A tuple containing the area and perimeter of the rectangle.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = 5
width = 3
area, perimeter = calculate_area_and_perimeter(length, width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

#16
def square_and_cube(number):
    """
    This function takes a number and returns a tuple containing the square and cube of the number.

    Parameters:
    number (int or float): The number to calculate the square and cube for.

    Returns:
    tuple: A tuple containing the square and the cube of the input number.
    """
    square = number ** 2
    cube = number ** 3
    return (square, cube)
num = 4
result = square_and_cube(num)
print(f"The square and cube of {num} are: {result}")

#17
def split_vowels_and_others(input_string):
    """
    This function takes a string as input and splits it into two parts:
    - One containing only the vowels (a, e, i, o, u).
    - The other containing all characters that are not vowels (consonants, spaces, etc.).

    Parameters:
    input_string (str): The input string to be split.

    Returns:
    tuple: A tuple containing two strings:
           - The first string contains all vowels from the input string.
           - The second string contains all non-vowel characters.
    """
    vowels = 'aeiouAEIOU' 
    vowels_part = ''
    others_part = ''
    for char in input_string:
        if char in vowels:
            vowels_part += char
        else:
            return (vowels_part, others_part)
input_str = "Hello World"
vowels, others = split_vowels_and_others(input_str)
print("Vowels part:", vowels)
print("Others part:", others)

#18
def separate_words_by_starting_letter(word_list):
    """
    This function takes a list of words and separates them into two lists:
    - One containing words that start with vowels (a, e, i, o, u).
    - The other containing words that start with consonants.

    Parameters:
    word_list (list): A list of words to be separated.

    Returns:
    tuple: A tuple containing two lists:
           - The first list contains words starting with vowels.
           - The second list contains words starting with consonants.
    """
    vowels = 'aeiouAEIOU'
    words_starting_with_vowels = []
    words_starting_with_consonants = []

    for word in word_list:
        if word[0].lower() in vowels:
            words_starting_with_vowels.append(word)
        else:
            words_starting_with_consonants.append(word)
    return (words_starting_with_vowels, words_starting_with_consonants)
word_list = ["apple", "banana", "orange", "umbrella", "grape", "kiwi", "egg"]
vowel_words, consonant_words = separate_words_by_starting_letter(word_list)
print("Words starting with vowels:", vowel_words)
print("Words starting with consonants:", consonant_words)
