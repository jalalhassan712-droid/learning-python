print("====== ATM MENU======")
print("1. Check Balance")
print("2. Deposit Money")   
print("3. Withdraw Money")
print("4. change pin")
print("5. Exit")
number = int(input("enter your choice :"))
total_amount = 10009
old_pin = 1234
match number:
    case 1:
        print(f"your total amount is : {total_amount}")
        
    case 2:
        deposit = int(input("enter you deposit amount :"))
        print(f"your deposit amount is : {deposit}")
        print(f"your total amount is : {total_amount + deposit}")
    case 3:
        withdraw = int(input("enter your withdraw amount :"))
        print(f"your withdraw amount is : {withdraw}")
        print(f"your total amount is : {total_amount - withdraw}")
    case 4:
        pin = int(input("enter your new pin :"))
        print(f"your old pin is : {old_pin}")
        print(f"your new pin is : {pin}")
    case 5:
        print("exit")
    case _:
        print ("invlaid choice ")
        