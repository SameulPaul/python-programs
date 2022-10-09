text = input("Enter Sentence to Analyze: ")

charcount = 0
wordcount = 0
for eachletter in list(text):
    if eachletter == " ": 
        wordcount = wordcount + 1
        charcount = charcount - 1

    charcount = charcount + 1
    
print("Word Count:", wordcount+1)
print("Character Count without spaces:", charcount)




