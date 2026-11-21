print("==========ATM managemnt system=========")
userid ="jalalhassan@"
pin=1234
total=10000

while True:
    admin=input ("enter your user id :")
    if admin==userid:
        
        passw=int(input("enter your pin"))
        if pin==passw:
            print("\n login succusfully ")
            while True:
                    
                    print("====== ATM MENU======")
                    print("1. Check Balance")
                    print("2. Deposit Money")   
                    print("3. Withdraw Money")
                    print("4. change pin")
                    print("5. Exit")
                    number=int(input("enter your choice :"))
                    
                    match number: 
                        case 1:
                            print(f"your total balance is : {total}")
                        case 2:
                            deposit = int(input("enter you deposit amount :"))
                            total+=deposit
                            print(f"your deposit amount is : {deposit}")
                            print(f"your total amount is : {total}")
                        case 3:
                            withdraw = int(input("enter your withdraw amount :"))
                            if withdraw<=total:
                                total-=withdraw
                                print(f"your withdraw amount is : {withdraw}")
                                print(f"your total amount is : {total }")
                            else:
                                print("Insufficient Balance")
                        case 4:
                            new_pin = int(input("enter your new pin :"))
                            new_pin=pin
                            if new_pin==pin:
                                print(f"your old pin is : {pin}")
                                print(f"your new pin is : {new_pin}")
                            else:
                                print("yur new pin is same to old")
                        case 5:
                            print("thank you for using atm")
                            break
                        case _:
                            print ("invlaid choice ")
            break                
                 
        else:
             print("than you for your serves")
    else:
        print("worng user id")

        




