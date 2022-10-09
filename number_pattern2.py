num = int(input("Enter Start Number in Pattern: "))
num1 = int(input("Enter Next Number in Pattern: "))

nextnum = num
for i in range(10):
    print(nextnum)
    if num1 > num:
        nextnum = nextnum + (num1 - num)
    else:
        nextnum = nextnum - (num - num1)
    
    




