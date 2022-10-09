num = input("Enter Number: ")


decimalflag = "N"
for eachchar in list(num):
    if eachchar == '.':
        decimalflag = "Y"
        break

if decimalflag == "Y":
    print("Number is Decimal")
else:
    print("Number is Integer")
    

    
    
    

        



