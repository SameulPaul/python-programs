text = input("Enter Text: ")
chartocount = input("Which Letter Do You Want To Count? ")

textlength = len(text)
charcount = 0

for i in range(textlength):
    if text[i] == chartocount:
        charcount = charcount + 1

print("Total Count Of Letter", chartocount, "in '", text, "' is:",charcount)


