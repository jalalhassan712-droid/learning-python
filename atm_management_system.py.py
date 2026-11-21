
print("========== ATM MANAGEMENT SYSTEM ==========")

userid = "jalalhassan@"
pin = "1234"
total = 10000

while True:
    admin = input("Enter your user ID: ")

    if admin == userid:

        passw = input("Enter your PIN: ")

        if passw == pin:
            print("\nLogin Successfully")

            while True:
                print("\n====== ATM MENU ======")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Change PIN")
                print("5. Exit")

                number = int(input("Enter your choice: "))

                match number:

                    case 1:
                        print(f"Your total balance is: {total}")

                    case 2:
                        deposit = int(input("Enter deposit amount: "))

                        if deposit > 0:
                            total += deposit
                            print(f"Your deposit amount is: {deposit}")
                            print(f"Your total balance is: {total}")
                        else:
                            print("Invalid deposit amount")

                    case 3:
                        withdraw = int(input("Enter withdrawal amount: "))

                        if withdraw > 0:
                            if withdraw <= total:
                                total -= withdraw
                                print(f"Your withdrawal amount is: {withdraw}")
                                print(f"Your total balance is: {total}")
                            else:
                                print("Insufficient Balance")
                        else:
                            print("Invalid withdrawal amount")

                    case 4:
                        new_pin = input("Enter your new PIN: ")

                        if new_pin != pin and len(new_pin) == 4 and new_pin.isdigit():
                            pin = new_pin
                            print("PIN changed successfully")
                        else:
                            print("Invalid PIN or same as old PIN")

                    case 5:
                        print("Thank you for using ATM")
                        break

                    case _:
                        print("Invalid choice")

            break

        else:
            print("Incorrect PIN")

    else:
        print("Wrong User ID")
