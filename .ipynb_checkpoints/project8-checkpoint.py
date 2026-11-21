user_id="admin"
password=1234
students=[]


def  login():
    
    while True:
        user=input("Enter your user id : ")    
        if user == user_id:
            pas=int(input("Enter your password : "))
            if pas==password:
                print("\nWelcome to University Management System")
                print("-----------------------------------")
                break
            else:
                print("Wrong password ")
        else:
            print("invalid user id ")

def add_student():
    roll_no = int(input("Enter Roll No            : "))

    
    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll Number Already Exists!")
            return

    name=input        ("Enter your name           :")
    age=int(input     ("Enter your age            : "))
    dep=(input        ("Enter your deparment name : "))
    semester=int(input("Enter your semester name  : "))
    cgpa=float(input    ("Enter your marks          :"))
    city=input        ("Enter your city name: ")
    
    
    student={
            "roll_no":roll_no,
            "name":name,
            "age":age,
            "dep":dep,
            "semester":semester,
            "cgpa":cgpa,
            "city":city
        }
    students.append(student)
    print("student data is added ")
    print("---------------------------------------")

def display():
    if len(students)==0:
        print("No student record found. ")
    else:
        for i in students:
            print("============= All student data =====================")
            print(f"roll no          :{i['roll_no']}")
            print(f"Name             :{i['name']}")
            print(f"age              :{i['age']}")
            print(f"dep              :{i['dep']}")
            print(f"semester         :{i['semester']}")
            print(f"CGPA             :{i['cgpa']}")
            print(f"city             :{i['city']}")
            print("-----------------------------------")
def search():
    rol=int(input("enter your roll no : "))
    found =False
    for i in students:
        if i["roll_no"]==rol:
            print("===========Student found ==========")
            print(f"roll no          :{i['roll_no']}")
            print(f"Name             :{i['name']}")
            print(f"age              :{i['age']}")
            print(f"dep              :{i['dep']}")
            print(f"semester         :{i['semester']}")
            print(f"CGPA             :{i['cgpa']}")
            print(f"city             :{i['city']}")
            print("-----------------------------------")
            found= True
            break
    if not found:
        print("student not found ")
def update():
    while True:
        print("what you want to update ")
        print("1.name ")
        print("2.age ")
        print("3.dep ")
        print("4.semester")
        print("5.cgpa")
        print("6. exit")
        choice=int(input("Enter your choice : "))
        match choice:
            case 1:
                rol=int(input("enter your roll no : "))
                found =False
                for i in students:
                    if i["roll_no"]==rol:
                        u_name=input("enter your name : ")
                        i["name"]=u_name
                        found=True
                        break
                if not found:
                    print("student not found")
            case 2:
                rol=int(input("enter your roll no : "))
                found =False
                for i in students:
                    if i["roll_no"]==rol:
                        u_age=int(input("enter your age : "))
                        i["age"]=u_age
                        found=True
                        break
                if not found:
                    print("student not found")
            case 3:
                rol=int(input("enter your roll no : "))
                found =False
                for i in students:
                    if i["roll_no"]==rol:
                        u_dep=input("enter your  dep name : ")
                        i["dep"]=u_dep
                        found=True
                        break
                if not found:
                     print("student not found")
            case 4:
                rol=int(input("enter your roll no : "))
                found =False
                for i in students:
                    if i["roll_no"]==rol:
                        u_semester=int(input("enter your semester name : "))
                        i["semester"]=u_semester
                        found=True
                        break
                if not found:
                     print("student not found")
            case 5:
                rol=int(input("enter your roll no : "))
                found =False
                for i in students:
                    if i["roll_no"]==rol:
                        u_cgpa=float(input("enter your cgpa : "))
                        i["cgpa"]=u_cgpa
                        found=True
                        break
                if not found:
                     print("student not found")


            case 6:
                print(" Student updated successfully.  ")
                print("-------------------------------")
                break
            case _:
                print("invalid choice")

def delete():
    rol=int(input("enter your roll no : "))
    found =False
    for i in students:
        if i["roll_no"]==rol:
            students.remove(i)
            print("student data is delete")
            print("---------------------------------")
            found=True
            break

    if not found:
        print("student is not found ")

def statistic():
    if len(students)==0:
        print("NO student record is found")
        return
    
    print("============= STATISTIC =============")
    print("Total student    :    ",len(students))
    highest = students[0]

    for i in students:
        if i["cgpa"] > highest["cgpa"]:
                highest = i

    print("Highest CGPA :", highest["cgpa"])
    print("Student Name :", highest["name"])
    lowest = students[0]

    for i in students:
        if i["cgpa"] < lowest["cgpa"]:
            lowest = i

    print("lowest CGPA  :", lowest["cgpa"])
    print("Student Name :", lowest["name"])
    if len(students) == 0:
        print("No student data available.")
    else:
        total = 0

        for i in students:
            total = total + i["cgpa"]

        average = total / len(students)

        print("Average CGPA :", average)



def main():
    
    while True:
            print(" \n========================================")
            print("      UNIVERSITY MANAGEMENT SYSTEM      ")
            print("========================================")
            print("1. Login")
            print("2. Add Student")
            print("3. Display Students")
            print("4. Search Student")
            print("5. Update Student")
            print("6. Delete Student")
            print("7. Statistics")
            print("8. Exit")
            
            choice=int(input("Enter your choice : "))
            match choice:
                case 1:
                    login()

                case 2:
                    add_student()

                case 3:
                    display()
                case 4:
                    search()
                case 5:
                    update()
                case 6:
                    delete()
                case 7 :
                    statistic()

                case 8:
                    print("thank you ")
                    break
                case _:
                    print("invalid choice  ")

main()