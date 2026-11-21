password= input("enter your password : ")
print("password entered")
print("========= password report==========")
print(f"password            : {password}")
print(f"password            : {len(password)}")
count_upper=0
for ch in password:
    if ch.isupper():
        count_upper+=1
    
print(f"upperacse latter    : {count_upper}")
count_lower=0
for ch in password:
    if ch.islower():
        count_lower+=1
print(f"lowercase latter    : {count_lower}")
count_digit=0
for ch in password:
    if ch.isdigit():
        count_digit+=1
print(f"digits              : {count_digit}")
count_sp=0
for ch in password:
    if ch in "@#$%*&^%+-!¬":
        count_sp+=1
print(f"special             : {count_sp}")
print(f"first               : {password[0]}")
print(f"last                : {password[-1]}")
print(f"reverse password    : {password[-1::-1]}")
print(f"every second        : {password[::2]}")
mid_password=password.replace("a", "*").replace("A","*")
print(f"modified password   : {mid_password}")
print("password status :  strong password  ")