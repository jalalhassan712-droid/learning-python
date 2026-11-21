print("====================================")
print("UNIVERSITY MANAGMENT SYSTEM ")
print("====================================")
print("login status ")
user = input("enter your user name ")
if user == "jalalhassan":
    password = input("enter your password")
    if password=="1234":
        print("login successfull ")
    
        print("personal information ")
        print("------------------------------")
        name = input("enter your name :")
        fname = input ("enter your fatherr name :")
        id = int(input("enter yout rol no "))
        cnic= int(input("enter yout cnic "))
        gender= input ("enter your gender (male /female)")
        age = int(input("enter your age "))
        print(f"your name is :        {name}")
        print(f"your father name is : {fname}")
        print(f"your id is :          {id}")
        print(f"your cnic is :        {cnic}")
        print(f"your are  :           {gender}")
        print(f"your age is   :       {age}")


        print ("ACADAMIC INFORMATION ")
        print("-------------------------------")
        python= int(input("enter your python marks"))
        cpp= int(input("enter your cpp marks"))
        html= int(input("enter your html marks"))
        css= int(input("enter your css marks"))
        print(f" your python marks is : {python}")         
        print(f" your cpp marks is :    {cpp}")         
        print(f" your html marks is :   {html}")         
        print(f" your css marks is :    {css}")         
        total= 400
        ob_marks=python+cpp+html+css
        per =( ob_marks*100)/total
        print(f"your total marks is : {total}")
        print(f"your obtain marks is :{ob_marks}")
        print(f"your percentage is : {per}")
        if per<= 90:
            print("grade A")
        elif per <= 80:
            print("grade B")
        elif per <= 60:
            print("grade C")
        else:
            print("fail")

        print("       attendence           ")
        print("-----------------------------")
        attendence = int(input("enter your attendence percentage"))
        if attendence >=75:
            print("you are eligible for exam ")
        else:
            print("short attendence")    

        print("      scholarship        ")
        print("--------------------------")
        if per>= 80 and attendence>= 90:
            print("you are eligiblle for schlarship")
        else:
            print("you are not eligible for scholarship")
        
    else:
        print("INCORECT PASSWORD ")
        
else:
    print("INCORECT USER NAME ")
   