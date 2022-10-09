num = input("Enter Number: ")


signflag = "N"
for eachchar in list(num):
    if eachchar == '-' or eachchar == '+':
        signflag = "Y"
        break

if signflag == "Y":
    print("Number is Signed")
else:
    print("Number is Unsigned")
    

    
    
    

        



