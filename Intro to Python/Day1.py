groceryList=["Congraulations! You created a grocery list."]
groceryNumber = int(input("How many things would you like to add to your grocery list? "))
for x in range (groceryNumber):
    x=x+1
    groceryList.append(input(f"What is number {x} in your grocery list? "))
    #make itemPlaceholder into a seperate variable each time
for y in range (groceryNumber):
    y=y+1
    #Call upon the previous variables created. If I can use the text in a string as a variable, then variable name + y = string and then call upon the string as a variable, it having the name of the one before. Number it too.

