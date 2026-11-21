
# ==========================================
# PYTHON USER INPUT
# ==========================================

# 1. Taking String Input

name = input("Enter your name: ")
print("Welcome", name)


# 2. Taking Integer Input

age = int(input("Enter your age: "))
print("Your age is:", age)


# 3. Taking Float Input

height = float(input("Enter your height: "))
print("Your height is:", height)


# 4. Type Checking Input

number = int(input("Enter a number: "))
print("Value:", number)
print("Data Type:", type(number))


# 5. Taking Multiple Inputs

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Full Name:", first_name, last_name)


# 6. User Input for Calculations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# 7. Calculating Area of Rectangle

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width

print("Area of Rectangle:", area)


# 8. Taking Multiple Values in One Line

a, b, c = input("Enter three values separated by spaces: ").split()

print("First Value:", a)
print("Second Value:", b)
print("Third Value:", c)


# 9. Converting Multiple Inputs into Integers

x, y = map(int, input("Enter two numbers: ").split())

print("Sum:", x + y)


# 10. User Input with F-Strings

student_name = input("Enter student name: ")
student_marks = float(input("Enter student marks: "))

print(f"Student Name: {student_name}")
print(f"Student Marks: {student_marks}")


# ==========================================
# END OF USER INPUT
# ==========================================
