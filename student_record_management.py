students={

}
n=input("Do you want any thing with list (yes/no )").lower()
if n=="yes":
    while True:
        print("=======================================")
        print("-------select your choice--------")
        print("1. Add Student")
        print("2. Display Studentst")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit \n")
        print(" ---------------------------------\n")
        choice=int(input("Enter your choice "))
        match choice:
            case 1:
                roll_no=int(input("Enter your roll no :"))
                name=input("Enter your name : ")
                age=int(input("Enter your age :"))
                semester=int(input("Enter your semester :"))
                marks=float(input("Enter your marks :"))
                if roll_no in students:
                    print("roll no already exists ")
                else:
                    students[roll_no]={
                        "name":name,
                        "age":age,
                        "semester":semester,
                        "marks":marks
                    }
                    print("student is data is added ")
                    print("---------------------------------")
            case 2:
                if len(students)==0:
                    print("the list is empty")
                else:
                    print("-------------All students data---------------")
                    for roll_no, i in students.items():
                        print(f"Roll no        : {roll_no}")
                        print(f"name           : {i['name']}")
                        print(f"age            : {i['age']}")
                        print(f"semester       : {i['semester']}")
                        print(f"marks          : {i['marks']}")
                        print("--------------------------------------")
            case 3:
                roll = int(input("Enter roll number: "))

                if roll in students:
                    print("Student Found")
                    print("----------------")
                    print("Name  :", students[roll]["name"])
                    print("Age   :", students[roll]["age"])
                    print("Marks :", students[roll]["marks"])
                else:
                    print("Student not found")
            case 4:
                 roll_no=int(input("enter your no"))
                 
                 if roll_no in students:
                        update_marks=int(input("enter your new marks : "))
                        students[roll_no]["marks"]=update_marks
                    

                 else:
                     print("wrong roll no ")
            
            case 6: 
                print("----------------------------")
                print("  Thank you  ")
                print("you are exit .")
                break
            case _ :
                print(" invalid choice ")

else:
    print("----------------thank you -----------------")