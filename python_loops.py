
# ==========================================
# PYTHON LOOPS
# ==========================================

# 1. While Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# 2. For Loop

for i in range(1, 6):
    print(i)


# 3. Range Function

# range(start, stop, step)

for i in range(1, 11, 2):
    print(i)


# 4. Reverse Loop

for i in range(10, 0, -1):
    print(i)


# 5. Nested Loops

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 6. Break Statement

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 7. Continue Statement

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 8. Pass Statement

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# 9. Else with For Loop

for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully.")


# 10. Else with While Loop

number = 1

while number <= 3:
    print(number)
    number += 1
else:
    print("While loop completed.")


# 11. Looping Through a String

name = "Python"

for character in name:
    print(character)


# 12. Looping Through a List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# 13. Looping Through a Dictionary

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 14. Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 15. Sum of First 10 Natural Numbers

total = 0

for i in range(1, 11):
    total += i

print("Total:", total)


# 16. List Comprehension

squares = [x ** 2 for x in range(1, 6)]

print("Squares:", squares)


# 17. Even Numbers Using List Comprehension

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even Numbers:", even_numbers)


# ==========================================
# END OF PYTHON LOOPS
# ==========================================
