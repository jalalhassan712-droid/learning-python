print("=================================")
print("          shopping menu          ")
print("=================================")
grand_total = 0
while True:
    print("\n========Shop menu========")
    print("1. Rice      = 250")
    print("2. Sugar     = 180")
    print("3. Milk      = 220")
    print("4. Bread     = 100")
    print("5. Eggs      = 300")
    print("6. Tea       = 450")
    print("7. Finish Shopping")
    choice=int(input("enter your choice :"))
    

    match choice:
        case 1:
            price=250
            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 2:
            price= 180
            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 3:
            price = 220
            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 4:
            price= 100
            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 5:
            price= 300
            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 6:
            price = 450

            quantity=int(input("enter your quantity : "))
            if quantity>0:
                item_total=price*quantity
                grand_total+=item_total
                print(f"your total bill {grand_total}")
            else:
                print("quantity cannot be negative or zero ")
        case 7:
            print("fininshed shopping ")
            break
        case _:

            print("invalid choice")
if grand_total >= 5000:
    discount = grand_total * 20 / 100

elif grand_total >= 3000:
    discount = grand_total * 10 / 100

elif grand_total >= 1000:
    discount = grand_total * 5 / 100

else:
    discount = 0
final_bil= grand_total- discount
print("==========final bill==========")
print("Total bill      : Rs.",grand_total)
print(f"discount       : Rs.{discount}")
print("Final bill      : Rs.",final_bil)

paid=int(input("\n enter your paid amount"))
if paid >=final_bil:
    change = paid-final_bil
    print(f"change return {change}")
    print("Thanks you for shopping with us ")
elif paid== final_bil:
    print("Thanks you for shopping with us ")
else:
    print("Insufficient Payment")





            
