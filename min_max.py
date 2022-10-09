count = int(input("Enter total numbers to be input: "))

numlist = []

if count <= 0:
    print("Count should be positive")
else:
    for i in range(count):
        num = int(input("Enter Number: "))
        numlist.append(num)
        
    #find min
    mini = numlist[0] #first as min
    for eachnum in numlist:
        if eachnum < mini:
            mini = eachnum

    print("Minimum is:",mini)
        
    #find max
    maxi = numlist[0] #first as max
    for eachnum in numlist:
        if eachnum > maxi:
            maxi = eachnum

    print("Maximum is:",maxi)
