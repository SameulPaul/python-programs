text = input("Enter Text: ")

textlength = len(text)

duplist = []
newtext = ""
for i in range(textlength):
    if text[i] not in duplist:
        newtext = newtext + text[i]
        duplist.append(text[i])
    

print("Text Without Duplicate Letters:", newtext)


