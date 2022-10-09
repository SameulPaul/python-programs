choice = input("Press O for Odd series and E for Even series: ")

for i in range(0,50):
    remainder = i%2
    if choice == 'e' or choice == 'E':
         if remainder == 0:
             print(i)
    elif choice == 'o' or choice == 'O':
        if remainder != 0:
             print(i)
    else:
        print("Invalid Choice")
        break
        
        
