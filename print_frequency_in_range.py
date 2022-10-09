startnum = int(input("Enter First Number in Sequence: "))
endnum = int(input("Enter Last Number in Sequence: "))
frequency = int(input("Enter Frequency Range: "))

for i in range(startnum, endnum+1):
    if i%frequency == 0:
        print(i)
