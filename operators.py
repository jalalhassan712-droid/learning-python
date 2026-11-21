
# ==========================================
# PYTHON OPERATORS
# ==========================================

# 1. Arithmetic Operators

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. Assignment Operators

x = 10

x += 5
print("Addition Assignment:", x)

x -= 3
print("Subtraction Assignment:", x)

x *= 2
print("Multiplication Assignment:", x)

x /= 4
print("Division Assignment:", x)

x //= 2
print("Floor Division Assignment:", x)

x %= 3
print("Modulus Assignment:", x)

x **= 2
print("Exponentiation Assignment:", x)


# 3. Comparison Operators

a = 20
b = 10

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)


# 4. Logical Operators

age = 20
marks = 85

print(age >= 18 and marks >= 50)
print(age >= 18 or marks >= 90)
print(not age < 18)


# 5. Bitwise Operators

a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# 6. Membership Operators

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("orange" not in fruits)


# 7. Identity Operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x == z)
print(x is not z)


# 8. Operator Precedence

result = 10 + 5 * 2
print("Multiplication First:", result)

result = (10 + 5) * 2
print("Parentheses First:", result)


# ==========================================
# END OF PYTHON OPERATORS
# ==========================================
