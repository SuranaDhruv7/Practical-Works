#Lab Work 3.1
"""
#1
First_name=str(input("Enter your first name: "))
Last_name=str(input("Enter your last name: "))
print(f"Hello[{Last_name}], [{First_name}]!")
"""

#2
"""
item=str(input("Enter your item: "))
price=float(input("Enter the price: "))
print(f"The price of {item} is {price} dollars")
"""

#3
"""
name="madam"
a=name[0:5]
b=name[::-1]
print(a,"The word is palindrome.")
print(b,"The word is palindrome.")
"""

#4
"""
user=str(input("Enter your name: "))
print(user.upper())
print(user.lower())
print(user.title())
"""

#5
"""
list=[1,2,3,4,5,6,7,8,9,10]
list.append(13)
print(list)
"""

#6
"""
user_input=input("Enter the items for the list, separated by commas: ")
user_list= user_input.split(",")
user_list= [item.strip() for item in user_list]
print("Your list is: ", user_list)
print("The largest number in the list is: ", max(user_list))
print("The smallest number in the list is: ", min(user_list))
"""

#7
"""
my_tuple = (1, 2, 2, 3, 4, 4, 5)
unique_values = set(my_tuple)
print("unique_value: ", unique_values)
"""

#8
"""
list1= [1,2,3,4,5]
list1[3]= 5
print(list1)
"""

#9
"""
list3=[1, 2, 3,[4, 5, 6],7, 8]
list3[4]=9
print(list3)
"""
#10
"""
my_list=[10, 20, 30, 40, 50,]
print("Original_list: ", my_list)
my_list.append(60)
print("After adding 60 at the end: ", my_list)
my_list.insert(2,25)
print("After adding 25 at index 2: ", my_list)
my_list[4] = 45
print("After replacing element at index 4 is 45: ", my_list)
my_list.remove(30)
print("After removing 30 from the list: ", my_list)
popped_element = my_list.pop(2)
print("After popping element at index 2: ", my_list)
print("Popped element: ", popped_element)
del my_list[1]
print("After deleting element at index 1: ", my_list)
"""

#11
"""
my_tuple = ([1, 2], [3, 4], [5, 6])
print("Original tuple: ", my_tuple)
my_tuple[1].append(7)
print("Modified tuple: ", my_tuple)
"""

#12
"""
a = 10
b = 20
print("Before swapping: ")
print("a =", a)
print("b =", b)
temp = a
a = b
b = temp
print("\nAfter swapping: ")
print("a =", a)
print("b =", b)
"""

#13
a = 10
b = 20
print("Before swapping: ")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("\n After swapping:")
print("a=", a)
print("b =", b)
