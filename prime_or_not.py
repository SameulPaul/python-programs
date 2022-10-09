num = input("Enter Number: ")


notprime = "N"
unitdigit = int(num)%10

if int(num) == 2 or int(num) == 3 or int(num) == 5:
    print("Number is Prime")
elif unitdigit == 0 or unitdigit == 2 or unitdigit == 4 or unitdigit == 6 or unitdigit == 8 or unitdigit == 5:
    print("Not a Prime")
else:
    digits = list(num)
    total = 0
    for i in digits:    
        total = total + int(i)

    if total%3 == 0:
        print("Not a Prime")
    else: #find square root
        i = int(num)
        numtosubtract = 1
        count = 0
        while i > 0: 
            i = i - numtosubtract
            numtosubtract = numtosubtract + 2
            count = count + 1
            
        for j in range(2,count):
            if int(num)%j == 0:
                print("Not a prime")
                notprime = "Y"
                break

        if notprime == "N":
            print("Number is Prime")
    
        

        



