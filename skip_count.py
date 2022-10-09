startnum = int(input("Enter First Number in Sequence: "))
endnum = int(input("Enter Last Number in Sequence: "))
skipcount = int(input("Enter Skip Count: "))

for i in range(startnum, endnum+1):
    if i%skipcount != 0:
        print(i)

