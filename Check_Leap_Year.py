year = int(input("Enter Year: "))

if year%4 != 0:
    print("Year is Not Leap Year")    
else:
    if year%100 == 0:
        if year%400 == 0:
            print("Year is Leap Year")    
        else:
            print("Year is Not Leap Year")    
    else:
        print("Year is Leap Year")    
    
    

