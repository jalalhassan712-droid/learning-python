student=[]
while True:
    print("========= STUDENT MENU =========")
    print("1. Add Student")      
    print("2. Display Students")      
    print("3. Search Student")      
    print("4. Update Student")      
    print("5. Delete Student")      
    print("6. Sort Students")      
    print("7. Reverse Students")      
    print("8. Count Students")      
    print("9. Copy Student List")      
    print("10. Exit") 
    choice=int(input("enter your choice : "))
    
    match choice:
        case 1:
            name = input("enter you name : ")
            roll_no = int(input("enter you roll no : "))
            marks = int(input("enter you marks : "))
          
            student.append([name,roll_no,marks])
            print("studnet added sucussfully ")
            print("----------------------------")
            
        case 2:
            if len(student)==0:
                 print("there is no student ")
            else:
                print("student list ")
                print("---------------------")
                for i in student:
                    print(f"name {i[0]}\t roll no {i[1]} \t marks {i[2]}")
        case 3:
            search=input("enter student name : ") 
            found = False
            for i in student:
                if i[0]==search:
                    print("student found ")
                    print("---------------")
                    print(f"student name    : {i[0]}")
                    print(f"student rool no : {i[1]}")
                    print(f"student marks   :  {i[2]}")
                    found=True
                    break
            else:
                    print("name not found in student list")
        case 4:
            search=input("enter student name : ")
            found= False
            for i in student:
                if i[0]==search:
                    print(" after update ")
                    print("---------------")
                    uodate=int(input("enter neew marks : "))
                    i[2]=uodate
                    
                    print(f"student marks   :  {uodate}")
                    print("Student updated successfully.")
                    found=True
                    break
            else:
                print("name not found in student list")
        case 5:
            search=input("enter student name : ")
            found=False
            for i in student:
                if i[0]==search:
                    print("student is deleted")
                    student.remove(i)
                    found=True
                    break
                
            else:
                 print("name not found in student list")
        case 6:
                    student.sort()
                    print("----------sorted---------- ")
                    for i in student:
                        print(i)
                    
        case 7:
                    student.reverse()
                    print("----------reverse---------- ")
                    for i in student:
                      print(i)
                    
        case 8:
            count_students=student.count()
            print("----------- count ---------------")
            print("total students are ",count_students)
            
        case 10:
            print("program end ")
            break
        case _:
            print("invalid choice ")



            