patien=[]
while True:
    print("======== HOSPITAL MANAGEMENT SYSTEM========\n")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patientt")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Sort Patients")
    print("7. Reverse Patient List")
    print("8. Count Patients")
    print("10. Find Oldest Patient")
    print("11. Find Youngest Patient")
    print("12. Show Admitted Patients")
    print("13. Show Discharged Patients")
    print("14. Exit")
    choice = int(input("enter your choice : "))
    match choice:
        case 1:
            print("patient data \n")
            print("-----------------------------------")
            name =input(" petient name     : ")
            id=int(input("patient id       : "))
            age = int(input("patient age   : "))
            disease=input("patient disease :")
            status=input("enter patient status :")
            patien.append([name,id,age,disease,status])
            print("\n patient data is entered")
            print("--------------------------------")
        case 2:
            if len(patien)==0:
                print("no patient record is available ")
            else:
                print("============ patient data ============")
                for i in patien:
                    print(f"name          : {i[0]} ")
                    print(f"id            : {i[1]} ")
                    print(f"age           : {i[2]} ")
                    print(f"diasease      : {i[3]} ")
                    print(f"status        : {i[4]}")
                    print("--------------------------------")

        case 3:
              
              search= input("Enter patien name ")
              found= False
              for i in patien:
                  if i[0]==search:
                    print("PATIENT FOUNDED")
                    print("patient name        :",i[0])
                    print("patient id          :",i[1])
                    print("patient age         :",i[2])
                    print("patient desease     :",i[3])
                    found=True
                    break
              if not found:
                    print("patient not found")

        case 4:
            n=input("Enter patient name :")
            found=False
            for i in patien:
                if i[0]==n:
                    u_desease=input("enter desaese : ")
                    u_status=input("enter status   : ")
                    i[3]=u_desease
                    i[4]=u_status
                    print("Data is updated")
                    print("------------------------------")
                    found=True
                    break
            if not found:
                     print("patient not found")
        case 5:
            n=input("enter patient name :")
            found=False
            for i in patien:
                if i[0]==n:
                    print("patietnt data is deleted ")
                    patien.remove(i)
                    print("------------------------------")
                    found=True
                    break
            else:
                print("patient i not found")

        case 6:
            print("------sorted data ---------")
            patien.sort()
            for i in patien:
                print(i)
            print("---------------------------")


        case 7:
            print("---------revere of data -----------")
            patien.reverse()
            for i in patien:
                print(i)
            print("-------------------------------------")

        case 8:
            print(f"\nTotal patien    :   {len(patien)}")
            print("-------------------------------")


        case 10:
            old=patien[0]
            found=False
            for i in patien:
                if i[2]>old[2]:
                    old=i
            print("=========oldest patient=========")
            print(f"name          : {old[0]} ")
            print(f"id            : {old[1]} ")
            print(f"age           : {old[2]} ")
            print(f"diasease      : {old[3]} ")
            print(f"status        : {old[4]} ")
            print("--------------------------------")
                    
                    

           
        case 11:
            young=patien[0]
            found=False
            for i in patien:
                if i[2]<young[2]:
                    young=i
            print("=========youngest patient=========")
            print(f"name          : {young[0]} ")
            print(f"id            : {young[1]} ")
            print(f"age           : {young[2]} ")
            print(f"diasease      : {young[3]} ")
            print(f"status        : {young[4]} ")
            print("--------------------------------")
        case 12 :
            old=patien[0]
            found=False
            for i in patien:
                if i[4]=="admitted":
                    odl=i
                    print("=========admitted patient=========")
                    print(f"name          : {i[0]} ")
                    print(f"id            : {i[1]} ")
                    print(f"age           : {i[2]} ")
                    print(f"diasease      : {i[3]} ")
                    print(f"status        : {i[4]} ")
                    print("--------------------------------")
                    found=True
                    
            if not found:
                        print("patient not found ")
                
        case 13 :
            old=patien[0]
            found=False
            for i in patien:
                if i[4]=="discharged":
                    odl=i
                    print("===========discharged patient=========")
                    print(f"name          : {i[0]} ")
                    print(f"id            : {i[1]} ")
                    print(f"age           : {i[2]} ")
                    print(f"diasease      : {i[3]} ")
                    print(f"status        : {i[4]} ")
                    print("--------------------------------")
                    found=True
                    
            if not found:
                    print("patient not found ")

        case 14:
            print("thank you for time ")
            break

