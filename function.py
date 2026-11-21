
# ==========================================
# PYTHON FUNCTIONS
# ==========================================

# 1. Defining and Calling a Function

def greet():
    print("Hello, Welcome to Python!")

greet()


# 2. Function with Parameters

def greet_user(name):
    print(f"Welcome {name}!")

greet_user("Ali")


# 3. Function with Multiple Parameters

def add(a, b):
    print("Addition:", a + b)

add(10, 20)


# 4. Function with Return Statement

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# 5. Default Arguments

def student(name, age=20):
    print("Name:", name)
    print("Age:", age)

student("Ahmed")
student("Ali", 22)


# 6. Keyword Arguments

def information(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

information(
    department="BSCS",
    name="Khan",
    age=21
)


# 7. Positional Arguments

def subtract(a, b):
    return a - b

print("Subtraction:", subtract(20, 10))


# 8. Multiple Return Values

def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(20, 10)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# 9. *args - Multiple Positional Arguments

def total(*args):
    print("Arguments:", args)
    print("Total:", sum(args))

total(10, 20, 30, 40, 50)


# 10. **kwargs - Multiple Keyword Arguments

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(
    name="Ali",
    age=20,
    department="BSCS"
)


# 11. Lambda Function

square = lambda x: x ** 2

print("Square:", square(5))


# Lambda with Multiple Arguments

addition = lambda a, b: a + b

print("Addition:", addition(10, 20))


# 12. Local Variable

def local_example():
    message = "I am a local variable"
    print(message)

local_example()


# 13. Global Variable

name = "Python"

def global_example():
    print("Global Variable:", name)

global_example()


# 14. Global Keyword

count = 10

def update_count():
    global count
    count = 20

update_count()
print("Updated Count:", count)


# 15. Recursive Function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# 16. Nested Functions

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    inner_function()

outer_function()


# 17. Passing a List to a Function

def display_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["Apple", "Banana", "Mango"]

display_fruits(my_fruits)


# 18. Passing a Dictionary to a Function

def display_student(student):
    for key, value in student.items():
        print(key, ":", value)

student = {
    "name": "Ahmed",
    "age": 21,
    "marks": 90
}

display_student(student)


# 19. Function with Conditional Statements

def check_even_odd(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

print(check_even_odd(10))
print(check_even_odd(7))


# 20. Function with a Loop

def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(5)


# ==========================================
# END OF PYTHON FUNCTIONS
# ==========================================
