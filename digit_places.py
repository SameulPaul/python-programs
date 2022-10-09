num = int(input("Enter Number Between 1 and 999: "))

hundreth = num//100
num = num % 100 #strip of 100th place
tenth = num//10
num = num % 10 #strip of 100th place
one = num//1

print("Digit in Hundreds-place is:",hundreth)
print("Digit in Tens-place is:",tenth)
print("Digit in Ones-place is:",one)

