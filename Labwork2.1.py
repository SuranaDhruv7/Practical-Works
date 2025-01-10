#1
"""
a=int(input("Enter the number: "))
if a%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
"""

#2
"""
age=int(input("Enter your the age: "))
if age <60:
    if age <12:
        print("Child")
    elif age <19:
        print("Teenager")
    else:
        print("Adult")
else:
    print("Senior")
"""
#3
"""
a=int(input("Enter your number: "))
b=int(input("Enter your number: "))
c=int(input("Enter your number: "))
if a>b:
    if a>c:
        print("a is max ")
    else:
        print("c is max ")
else:
    if b>c:
        print("b is max ")
    else:
        print("c is max")
"""

#4
"""
user_1 = int(input("Enter the number: "))
user_2 = int(input("Enter the number: "))
operations = input("Enter the operation (+,-,*,/): ")
if operations == '+':
    result = user_1 + user_2
    print("The sum is: ", result)
elif operations == '-':
    result = user_1 - user_2
    print("The sub is: ", result)
elif operations == '*':
    result = user_1 * user_2
    print("The multiplication is: ", result)
elif operation == '/':
    if num2 != 0:
        result = num1/num2
        print("The result of division is: ", result)
    else:
        print("Error: Devision by zero is not allowed.")
else:
    print("Invalid operation. Please enter =,-,*, or /.")
"""
#5
"""
i=int(input("Enter your number: "))
while i<= 10:
    print(i)
    i+=1
"""

#6
"""
for i in range(1,11,1):
    print(i**2)
"""

#7
"""
i=1
while i <= 50:
    if i%2 == 0:
        print(i)
    i = i + 1
"""

#8
"""
for i in range (1,21,1):
    print(i)

for i in range (1,21,1):
    if i%2 == 1:
        print(i)
"""

#9
"""
for i in range (5,51,5):
    print(i)
"""

#10
"""
for i in range (10,0,-1):
    print(i)
"""

#11
for i in range(1,51):
    if i%2 ==0 and i%3 ==0:
        print(i,":- Both are divisible by 2 and 3")
    elif i%2 == 0 and i%3 != 0:
        print(i,":- The number is divisible by 2")
    elif i%2 != 0 and i%3 == 0:
        print(i,":- The number is divisible by 2")
    else:
        print(i)
            
