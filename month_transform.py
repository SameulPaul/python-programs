inputmonth = int(input("Enter a month in number between 1 and 12: "))

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
monthfound = 'N'
i = 1
for eachmon in months:
    if i == inputmonth:
        print("Month is:",eachmon)
        monthfound = 'Y'        
        break
    i = i + 1

if monthfound =='N':
    print("Invalid Month Number")
