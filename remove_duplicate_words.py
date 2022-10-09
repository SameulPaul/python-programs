text = input("Enter Sentence: ")

textlength = len(text)

duplist = []
newtext = ""
for eachword in text.split():
    if eachword not in duplist:
        newtext = newtext + eachword + " "
        duplist.append(eachword)
    

print("Text Without Duplicate Words:", newtext)


