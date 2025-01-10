#1
"""
array = int(input("Enter the number: "))
for i in str(array):
    print(i)
"""

#2
"""
array = []
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
for i in range(rows):
    array.append([])
    for j in range(cols):
        array[i].append(int(input("Enter elem: ")))
for i in array:
    for j in i:
        print(j, end = " ")
    print()

#3
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = []
print("Enter the elements of a 2x3 matrix:")
for i in range(2):
    row = []
    for j in range(3):
        value = int(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(value)
    matrix.append(row)

print("\nOriginal 2x3 Matrix:")
for row in matrix:
    print(row)
transposed_matrix = transpose_matrix(matrix)
print("\nTransposed 3x2 Matrix:")
for row in transposed_matrix:
    print(row)

#4
array = []
n = int(input("Enter how many elements: "))
for i in range(n):
    elem = int(input("Enter elem: "))
    array.append(elem)
sum = 0
for i in array:
    sum += i
print(sum)

#5
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array = []
print("Enter the elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element for position ({i+1},{j+1}): ")))
    array.append(row)
total_sum = 0
for i in array:
    for j in i:
        total_sum += j
print(f"\nThe sum of all elements in the 2D array is: {total_sum}")

#6
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array = []
print("Enter the elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element for position ({i+1},{j+1}): ")))
    array.append(row)
max_value = float(-ing) 
min_value = float(ing)

#7
array = []
n = int(input("Enter how many elements: "))
for i in range(n):
    elem = int(input("Enter elem: "))
    array.append(elem)
num1 = int(input("Enter the index value :-- "))
num2 = int(input("Enter the value / position you want to change/insert :-- "))
array[num1] = num2
print(array)

#8
def delete_element(arr, value):
    if value in arr:
        arr.remove(value)
        print(f"Element {value} removed successfully. ")
    else:
        print(f"Element {value} not found in the array.")
def main():
    arr = list(map(int, input("Enter the elements of the array (seperated by spaces): ")).split())
    value_to_remove = int(input("Enter the value to delete: "))
    print("Original array: ", arr)
    delete_element(arr, value_to_remove)
    print("Updated array: ", arr)
#9
def update_element(array, index, new_value):
    if 0 <= index < len(array):
        array[index] = new_value
        print(f"Element at index {index} has been updated to {new_value}.")
    else:
        print(f"Error: Index {index} is out of bounds.")
    return array
array = [10, 20, 30, 40, 50]
print("Original array:", array)
index = int(input("Enter the index of the element to update: "))
new_value = int(input("Enter the new value: "))
updated_array = update_element(array, index, new_value)
print("Updated array:", updated_array)

#10
def search_element(array, element):
    if element in array:
        return array.index(element)
    else:
        return -1
array = [10, 20, 30, 40, 50]

print("Array:", array)

element = int(input("Enter the element to search for: "))
index = search_element(array, element)

if index != -1:
    print(f"The element {element} is found at index {index}.")
else:
    print(f"The element {element} is not found in the array.")

#11
def concatenate_arrays(array1, array2):
    return array1 + array2

array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
print("Array 1:", array1)
print("Array 2:", array2)
result = concatenate_arrays(array1, array2)
print("Concatenated Array:", result)

#12
def sort_list_ascending(input_list):
    input_list.sort()
    return input_list

numbers = [5, 2, 8, 1, 3, 7, 4]
print("Original List:", numbers)
sorted_numbers = sort_list_ascending(numbers)
print("Sorted List in Ascending Order:", sorted_numbers)

#13
def sort_tuples_by_second_element(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[1])
    return sorted_list

tuples = [(1, 3), (4, 1), (2, 5), (7, 2), (3, 8)]

print("Original List of Tuples:", tuples)
sorted_tuples = sort_tuples_by_second_element(tuples)
print("Sorted List of Tuples based on the Second Element:", sorted_tuples)

#14
def sort_dicts_by_key(dict_list, key):
    sorted_list = sorted(dict_list, key=lambda x: x[key])
    return sorted_list

dicts = [
    {'name': 'Alice', 'age': 30, 'salary': 50000},
    {'name': 'Bob', 'age': 25, 'salary': 60000},
    {'name': 'Charlie', 'age': 35, 'salary': 45000},
    {'name': 'David', 'age': 28, 'salary': 55000}
]

print("Original List of Dictionaries:", dicts)
sorted_dicts_by_age = sort_dicts_by_key(dicts, 'age')

print("Sorted List of Dictionaries by Age:", sorted_dicts_by_age)
sorted_dicts_by_salary = sort_dicts_by_key(dicts, 'salary')
print("Sorted List of Dictionaries by Salary:", sorted_dicts_by_salary)
"""

#15
sample_list = [7, 2, 9, 4, 5, 1, 8, 6, 3]
print("Original List:", sample_list)

sample_list.sort()
print("List after sort() (in-place):", sample_list)

sample_list = [7, 2, 9, 4, 5, 1, 8, 6, 3]
print("\nRestored Original List:", sample_list)

sorted_list = sorted(sample_list)
print("List after sorted() (returns a new list):", sorted_list)
print("Original List after sorted() (unchanged):", sample_list)