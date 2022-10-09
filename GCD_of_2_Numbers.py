num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    remainder = num1
    dividend = num1
    divisor = num2
else:
    remainder = num2
    divident = num2
    divisor = num1

while remainder > 0:
    newdividend = dividend // divisor
    remainder = dividend%divisor
    if remainder == 0:        
        break
    dividend = divisor
    divisor = remainder
    
print("GCD is:",divisor)
    
    
    

        



