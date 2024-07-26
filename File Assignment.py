listOfText=[]
with open("Files/MyTextThing.txt","r") as beans:
    for i in beans:
        listOfText.append(i.split(" "))
        if (listOfText[i][-1]=="\n"):
            
print(listOfText)
with open("Files/MyTextOutputThing.txt","a") as beans2:
    for i in listOfText:
        for k in i:
            beans2.write(str(k)+" ")