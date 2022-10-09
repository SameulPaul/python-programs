num = input("Enter a number to check if Armstrong Number: ")

digits = list(num)

total = 0
for i in digits:
    digittotal = 1
    for j in range(len(digits)):
        digittotal = digittotal * int(i)
    total = total + digittotal
    
if total == int(num):
    print("Number is an Armstrong Number")
else:
    print("Number is not an Armstrong Number")
    
    

