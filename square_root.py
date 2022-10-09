num = int(input("Enter Number for which Square Root is required: "))

i = num
numtosubtract = 1
count = 0
while i > 0:
    i = i - numtosubtract
    numtosubtract = numtosubtract + 2
    count = count + 1
    

if i == 0:
    print(count)
else:
    print('Not a perfect square')
    
    




