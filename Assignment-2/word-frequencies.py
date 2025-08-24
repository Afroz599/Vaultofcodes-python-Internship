#splitting the text into words
Text=input("enter any text here\n").split(' ')
#user enters the word to be searched for
Word=input("enter the word you want to find the count of...\n")
count=0
#iteration till the end word
for w in Text:
  #comparing the words with given word
    if w==Word:
      #increment on the successful finding
        count+=1
if count>0:
  print(f"word {Word} appeared in the text for {count} times")
else:
  print(f"word{Word} is not present in the text")
