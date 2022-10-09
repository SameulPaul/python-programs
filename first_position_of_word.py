text = input("Enter Sentence: ")
wordsearch = input("Enter Word to find position: ")

wordfound = "N"
i = 1
for eachword in text.split():
    if eachword == wordsearch:        
        wordfound = "Y"
        break
    i = i + 1

if wordfound == "Y":
    print(wordsearch,"Is in Position", i)
else:
    print("Word not found in sentence")




