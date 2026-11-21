
# ==========================================
# PYTHON DATA STRUCTURES
# LISTS, TUPLES, SETS, DICTIONARIES
# ==========================================


# ==========================================
# 1. LISTS
# ==========================================

# Creating a List

fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Fruits:", fruits)

# Accessing List Elements

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# List Slicing

print("Slicing:", fruits[1:3])

# Updating List Elements

fruits[1] = "Grapes"
print("Updated List:", fruits)

# Adding Elements

fruits.append("Watermelon")
print("Append:", fruits)

fruits.insert(1, "Pineapple")
print("Insert:", fruits)

fruits.extend(["Peach", "Cherry"])
print("Extend:", fruits)

# Removing Elements

fruits.remove("Mango")
print("Remove:", fruits)

fruits.pop()
print("Pop:", fruits)

del fruits[0]
print("Delete:", fruits)

# List Methods

numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Count:", numbers.count(5))

# Searching in List

if 8 in numbers:
    print("8 is present in the list.")

# Copying a List

original = [10, 20, 30]
copied = original.copy()

print("Original:", original)
print("Copied:", copied)

# Looping Through a List

for fruit in fruits:
    print(fruit)

# List Comprehension

squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even Numbers:", even_numbers)


# ==========================================
# 2. TUPLES
# ==========================================

# Creating a Tuple

colors = ("Red", "Green", "Blue", "Yellow")
print("Colors:", colors)

# Accessing Tuple Elements

print("First Color:", colors[0])
print("Last Color:", colors[-1])

# Tuple Slicing

print("Slicing:", colors[1:3])

# Tuple Methods

numbers_tuple = (10, 20, 30, 20, 40, 20)

print("Count:", numbers_tuple.count(20))
print("Index:", numbers_tuple.index(30))

# Tuple Length

print("Length:", len(colors))

# Tuple Packing

student = ("Ali", 20, "BSCS")

# Tuple Unpacking

name, age, department = student

print("Name:", name)
print("Age:", age)
print("Department:", department)

# Single Element Tuple

single = (10,)
print("Single Element Tuple:", single)


# ==========================================
# 3. SETS
# ==========================================

# Creating a Set

numbers_set = {10, 20, 30, 40, 20}
print("Set:", numbers_set)

# Adding Elements

numbers_set.add(50)
print("After Add:", numbers_set)

# Updating a Set

numbers_set.update([60, 70, 80])
print("After Update:", numbers_set)

# Removing Elements

numbers_set.remove(20)
print("After Remove:", numbers_set)

numbers_set.discard(100)
print("After Discard:", numbers_set)

# Set Operations

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union

print("Union:", set_a.union(set_b))

# Intersection

print("Intersection:", set_a.intersection(set_b))

# Difference

print("Difference:", set_a.difference(set_b))

# Symmetric Difference

print("Symmetric Difference:",
      set_a.symmetric_difference(set_b))

# Subset and Superset

small = {1, 2}
large = {1, 2, 3, 4}

print("Subset:", small.issubset(large))
print("Superset:", large.issuperset(small))

# Membership

print("Is 3 Present:", 3 in set_a)

# Set Length

print("Set Length:", len(set_a))

# Looping Through a Set

for item in set_a:
    print(item)


# ==========================================
# 4. DICTIONARIES
# ==========================================

# Creating a Dictionary

student = {
    "name": "Ali",
    "age": 20,
    "department": "BSCS",
    "marks": 85
}

print("Student:", student)

# Accessing Values

print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding New Items

student["city"] = "Peshawar"
print("After Adding:", student)

# Updating Values

student["marks"] = 90
student.update({"age": 21})

print("After Updating:", student)

# Removing Items

student.pop("city")
print("After Pop:", student)

student.popitem()
print("After Popitem:", student)

# Dictionary Methods

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Checking Keys

if "name" in student:
    print("Name key exists.")

# Looping Through Dictionary

for key in student:
    print(key, student[key])

# Looping Through Keys and Values

for key, value in student.items():
    print(key, ":", value)

# Copying Dictionary

original = {"name": "Ahmed", "age": 22}
copied = original.copy()

print("Copied Dictionary:", copied)

# Nested Dictionary

students = {
    "student1": {
        "name": "Ali",
        "marks": 85
    },
    "student2": {
        "name": "Ahmed",
        "marks": 90
    }
}

print("Student 1:", students["student1"]["name"])
print("Student 2 Marks:", students["student2"]["marks"])

# Dictionary Comprehension

squares_dict = {x: x ** 2 for x in range(1, 6)}

print("Squares Dictionary:", squares_dict)


# ==========================================
# END OF PYTHON DATA STRUCTURES
# ==========================================
