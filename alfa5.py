manushowProduc = 1 

menubuyProduc = 2 

productName =3 

productPrice = 180 

userBalanc = int (input("Enter ammout"))

userCommand = int (input("Enter command"))

if (userCommand ==1):
    print("Name " , productName )
    print("Price ", productPrice)

if (userCommand ==2 ): 
    if (userCommand >= productPrice):
        print("You bought the prodoct")
    if (userBalanc < productPrice):
        print("you dont have enough balanc ")

if (userCommand == 3 ):
    print("good buy") 