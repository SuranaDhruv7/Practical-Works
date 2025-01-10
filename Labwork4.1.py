#1
"""
list1 = [1, 2, 3, 4, 5, 6, 7]
print(len(list1))
print(max(list1))
print(sorted(list1))
print(sum(list1))
print(type(list1))
"""

#2
"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}")
factorial(6)
"""

#3
"""
def square_integer(input_list):
    return [i**2 for i in input_list]
input_list = [12, 13, 14, 15, 16, 17]
squared_list = square_integer(input_list)
print(f"Original list: ", input_list)
print(f"Squared list: ", squared_list)
"""

#4
"""
def character(input_string):
    frequency = {}
    for character in input_string:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency
string = "David!"
print(character(string))
"""

#5
"""
def cube(x):
    return x**3
def process_numbers(numbers, func):
    return [func(num) for num in numbers]
numbers_list = [1, 2, 3, 4, 5]
result = process_numbers(numbers_list, cube)
print(f"Cubes of the numbers: {result}")
"""

#6
"""
def sumo(*dude):
    sum = 0
    for i in dude:
        sum = sum + i
    return sum
def cool(*boy):
    sum = 1
    for i in boy:
        sum = sum *i
    return sum
a= sumo(1,2,3,4,5,6)
b= cool(1,2,3,4,5,6)
print(a)
print(b)

#7
# Function to print student names, using *args to accept multiple names
def print_student_names(*args):
    # Check if any names are provided
    if len(args) == 0:
        print("No student names were provided.")
    else:
        # Print each student name on a new line
        print("List of Student Names:")
        for name in args:
            print(name)

# Example usage
print_student_names("John", "Alice", "Bob", "Charlie")  # Pass some student names
print_student_names()  # Call with no names to test the empty list condition

#8
def filter_values(*args):
    strings = []
    numbers = []
    
    for item in args:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
    
    return tuple(strings), tuple(numbers)

strings_tuple, numbers_tuple = filter_values("John", 25, "Alice", 30.5, 42, "Bob", 60)
print("Strings:", strings_tuple)
print("Numbers:", numbers_tuple)

#9
def print_person_description(**kwargs):
    description = "Person Description:\n"
    
    for key, value in kwargs.items():
        description += f"{key.capitalize()}: {value}\n"
    
    print(description)
print_person_description(name="John Doe", age=30, city="New York", profession="Engineer")
#10
def calculate_total_cost(**products):
    total_cost = 0

    for product, details in products.items():
        name = details.get('name')
        price = details.get('price')
        quantity = details.get('quantity')
        
        if price is not None and quantity is not None:
            cost = price * quantity  
            total_cost += cost 
            print(f"{name}: ${price} x {quantity} = ${cost:.2f}")

    return f"Total cost of all products: ${total_cost:.2f}"

product_details = {
    "product1": {"name": "Laptop", "price": 1000, "quantity": 2},
    "product2": {"name": "Headphones", "price": 150, "quantity": 3},
    "product3": {"name": "Keyboard", "price": 50, "quantity": 1}
}

result = calculate_total_cost(**product_details)
print(result)

#11
def create_employee_profile(**employee_details):
    required_fields = ['name', 'department', 'salary']
    
    missing_fields = [field for field in required_fields if field not in employee_details]
    
    if missing_fields:
        print(f"Missing required fields: {', '.join(missing_fields)}")
        return None

    print("\nEmployee Profile:")
    for key, value in employee_details.items():
        print(f"{key.capitalize()}: {value}")

employee1 = create_employee_profile(name="John Doe", department="Engineering", salary=70000)
print("\n" + "="*30 + "\n")
employee2 = create_employee_profile(name="Alice Smith", salary=60000)  # Missing department
"""

#12
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float or int): The length of the rectangle.
    width (float or int): The width of the rectangle.

    Returns:
    float: The area of the rectangle (length * width).
    """
    return length * width

length = 5
width = 3
area = calculate_area(length, width)

print(f"The area of the rectangle is: {area}")

print("\nFunction Documentation:")
print(calculate_area.__doc__)

#13
def fibonacci_sequence(limit):
    """
    Generate the Fibonacci sequence up to a given number.

    Parameters:
    limit (int): The upper limit of the Fibonacci sequence. The sequence will stop when a number exceeds this limit.

    Returns:
    list: A list containing the Fibonacci sequence up to the given limit.
    
    Example:
    fibonacci_sequence(10) will return [0, 1, 1, 2, 3, 5, 8]
    """
    
    sequence = [0, 1]
    
    while True:
        next_number = sequence[-1] + sequence[-2]
        if next_number > limit:
            break
        sequence.append(next_number)
    
    return sequence

limit = int(input("Enter the limit up to which you want the Fibonacci sequence: "))
fib_sequence = fibonacci_sequence(limit)

print(f"The Fibonacci sequence up to {limit} is: {fib_sequence}")

print("\nFunction Documentation:")
print(fibonacci_sequence.__doc__)