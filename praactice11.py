admin="jalalhassan"
password= "1234"
while True:
    userid = input("enter your userid :")
    

    if userid==admin:
        
        password = input("enter your password :")
        if password == "1234":
           
            print("you are login suucessfully")
            break
          
        else:
             print("your password is not correct")
    else:
            print("your user id  is not correct")

  
    