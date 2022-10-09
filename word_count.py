text = input("Enter Sentence: ")

textlength = len(text)
wordcount = 0

for i in range(textlength):
    if text[i] == " " and text[i+1] != " ":
        wordcount = wordcount + 1

print("Total Words In Sentence",wordcount+1)


