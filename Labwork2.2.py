#1
"""
for i in range(1,21):
    if i%4 == 0 :
        continue
    print(i)
"""

#2
"""
i=1
while i<=10:
    if i== 7:
        break
    print(i)
    i+=1
"""

#3
"""
String= "PYTHON"
for i in String:
    if i=="A"or i=="E"or i=="I"or i=="O"or i=="U":
        continue
    print(i)
"""

#4
"""
basket=[i**3 for i in range(1,11)]
print(basket)
"""

#5
"""
basket=[i for i in range(1,51) if i%2 == 0]
print(basket)
"""

#6
"""
def filter_words_starting_with_vowel(words):
    vowels= "AEIOU"
    return [word for word in words if word[0] in vowels]
basket=["Apple", "Banana", "Orange", "Elephant", "Umbrella", "Ice cream"]
filtered_words = filter_words_starting_with_vowel(basket)
print("Words starting with a vowel: ", filtered_words)
"""

#7
"""
for i in range(1,6):
    for j in range(1, i+1):
        print('*', end = '', sep = " ")
    print()
"""

#8
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print('*', end = '', sep = " ")
    print()
"""

#9
"""
for i in range(1,6):
    for k in range(5, i, -1):
        print(" _  ", end="")
    for j in range(1,i+1):
        print(i, end = "", sep = " ")
    print()
"""

#10
for table in range(1, 6):
    print("Multiplication Table for ", table)
    for multiplier in range(1,11):
        result = table * multiplier
        print(f"{table} x {multiplier} = {result}")
    print("_" * 20)
