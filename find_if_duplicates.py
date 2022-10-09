count = int(input("Enter total numbers to be input: "))

numlist = []

if count <= 0:
    print("Count should be positive")
else:
    for i in range(count):
        num = int(input("Enter Number: "))
        numlist.append(num)
        
    #find if duplicates present
    currentitem = 0
    dupflag = 'N'
    for eachnum in numlist: #for each number in list        
        for i in range(count): #go through remaining items in list
            if i != currentitem: #skip processing current item
                if eachnum == numlist[i]: #compare our number with current item in list                    
                    dupflag = 'Y'
                    break
        currentitem = currentitem + 1

    if dupflag == 'Y':
        print('Duplicates Present')
    else:
        print('No Duplicates')
    
                
