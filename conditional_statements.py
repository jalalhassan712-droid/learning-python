
# ==========================================
# PYTHON CONDITIONAL STATEMENTS
# ==========================================

# 1. Simple If Statement

age = 20

if age >= 18:
    print("You are eligible to vote.")


# 2. If-Else Statement

number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 3. If-Elif-Else Statement

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# 4. Nested If Statement

age = 22
has_id_card = True

if age >= 18:
    if has_id_card:
        print("You can enter.")
    else:
        print("ID card is required.")
else:
    print("You are underage.")


# 5. Using AND Operator

age = 21
marks = 75

if age >= 18 and marks >= 50:
    print("You are eligible.")
else:
    print("You are not eligible.")


# 6. Using OR Operator

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's a weekend.")
else:
    print("It's a working day.")


# 7. Using NOT Operator

is_raining = False

if not is_raining:
    print("You can go outside.")
else:
    print("Take an umbrella.")


# 8. Comparison Operators

a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 9. Match-Case Statement

choice = 2

match choice:
    case 1:
        print("Home")
    case 2:
        print("About")
    case 3:
        print("Contact")
    case _:
        print("Invalid choice")


# 10. Ternary Operator

age = 19

result = "Adult" if age >= 18 else "Minor"

print(result)


# ==========================================
# END OF CONDITIONAL STATEMENTS
# ==========================================
