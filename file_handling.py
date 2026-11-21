
# ==========================================
# PYTHON FILE HANDLING
# ==========================================

# 1. Opening and Closing a File

file = open("example.txt", "w")
file.write("Hello, Welcome to Python File Handling!")
file.close()


# 2. Reading a File

file = open("example.txt", "r")
content = file.read()
print("File Content:", content)
file.close()


# 3. Writing to a File

# Write mode creates a file or overwrites existing content.

file = open("example.txt", "w")
file.write("Python is a powerful programming language.")
file.close()


# 4. Appending Data to a File

# Append mode adds content at the end.

file = open("example.txt", "a")
file.write("\nI am learning File Handling.")
file.close()


# 5. Reading the Complete File

file = open("example.txt", "r")
content = file.read()

print("Complete Content:")
print(content)

file.close()


# 6. Reading a Specific Number of Characters

file = open("example.txt", "r")
content = file.read(10)

print("First 10 Characters:", content)

file.close()


# 7. Reading One Line

file = open("example.txt", "r")
line = file.readline()

print("First Line:", line)

file.close()


# 8. Reading All Lines

file = open("example.txt", "r")
lines = file.readlines()

print("All Lines:", lines)

file.close()


# 9. Reading File Line by Line

file = open("example.txt", "r")

for line in file:
    print(line.strip())

file.close()


# 10. Writing Multiple Lines

lines = [
    "Python\n",
    "NumPy\n",
    "Pandas\n",
    "Machine Learning\n"
]

file = open("subjects.txt", "w")
file.writelines(lines)
file.close()


# 11. Using with open()

# Automatically closes the file.

with open("example.txt", "r") as file:
    content = file.read()
    print("Using With:", content)


# 12. Using Different File Modes

# r = Read
# w = Write
# a = Append
# x = Create

with open("new_file.txt", "x") as file:
    file.write("This is a newly created file.")

# Use x mode only when the file does not already exist.


# 13. Checking Whether a File Exists

import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# 14. Getting File Information

if os.path.exists("example.txt"):
    print("File Size:", os.path.getsize("example.txt"), "bytes")


# 15. Exception Handling with Files

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")


# 16. Working with File Paths

file_path = "example.txt"

if os.path.isfile(file_path):
    print("This is a file.")

if os.path.isdir("."):
    print("Current directory exists.")


# 17. Binary File Handling

# Binary mode is commonly used for images and other binary files.

# Example:
# with open("image.jpg", "rb") as file:
#     data = file.read()

# with open("image_copy.jpg", "wb") as file:
#     file.write(data)


# 18. Deleting a File

# Be careful: this permanently deletes the file.

# if os.path.exists("old_file.txt"):
#     os.remove("old_file.txt")
#     print("File deleted.")


# ==========================================
# END OF PYTHON FILE HANDLING
# ==========================================
