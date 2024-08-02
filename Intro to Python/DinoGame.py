import copy
def printMap(theMap):
    for i in range (len(myMap)):
        for k in range (len(myMap[i])):
            print(myMap[i][k],end="")
        print(" ")
redo=True
mapCollection=[[[" "," ","█","█","█","█","█"," "],["█","█","█"," "," "," ","█"," "],["█","◯","◆","□"," "," ","█"," "],["█","█","█"," ","□","◯","█"," "],["█","◯","█","█","□"," ","█"," "],["█"," ","█"," ","◯"," ","█","█"],["█","□"," ","⧇","□","□","◯","█"],["█"," "," "," ","◯"," "," ","█"],["█","█","█","█","█","█","█","█"]],[["█","□","█","█","█","█","█"],["█","□"," ","□","◆","◯","█"],["□","□"," "," ","█"," ","█"],["█","□","█"," ","█","◯","█"],["█"," ","□"," ","█","□","█"],["█","◯","█"," "," ","□","□"],["█","█","█","█","█","█","█"]],[["◆","□","◯","█"," ","□","█"],["□","□"," ","█","□","□","█"],["◯","█"," ","□","□","□","□"],["█","□","◯"," ","█","□","□"],["█","□"," ","█","█","█","□"],["□","□","□","□","□","□","□"]]]
while (redo==True):
    print("\nThe point of this game is to cover up all pressure plates with squares by moving them\n\n█ is an immovable block\n□ is a movable block\n◯ is a pressure plate\n⧇ is a movable block with a pressure plate underneath\n◆ is the player\n⟐ is the player on top of a pressure plate\n\nPlease don't softlock yourself")
    win=False
    while(True):
        try:
            mapNum=float(str(input(f"There are {len(mapCollection)} maps to choose from, which one do you want? ")))-1
            if(int(mapNum)==mapNum):
                mapNum=int(mapNum)
            elif(mapNum+1<len(mapCollection) and mapNum>-1):
                pass
            else:
                KeyboardInterrupt
            break
        except:
            print("Put a natural number that is inside of the range please.")
    myMap=copy.deepcopy(mapCollection[mapNum])
    checkMap=copy.deepcopy(myMap)
    printMap(myMap)
    surrender=False
    while(win==False):
        try:
            pInput=input("What move would you like to do? (Quit is an option) ").upper()
            if(pInput not in ("W","A","S","D","QUIT")):
                print('Just put "W", "A", "S", "D", or "Quit".')
            else:
                works=True
            if(pInput=="QUIT"):
                surrender=True
        except:
            print("Please enter something.")
        if (surrender==True):
            break
        for i in range(len(myMap)):
            for k in range(len(myMap[i])):
                if(myMap[i][k]=="⧇"):
                    myMap[i][k]="□"
                if(myMap[i][k]=="⟐"):
                    myMap[i][k]="◆"
                if(myMap[i][k]=="◯"):
                    myMap[i][k]=" "
        checkBoardMove=copy.deepcopy(myMap)
        for i in range (len(myMap)):
            if (myMap[i].count("◆")!=0 and checkBoardMove==myMap):
                pColumn=myMap[i].index("◆")
                if(pInput=="W"):
                    if(i==0):
                        print("Don't throw yourself off the edge now.")
                        works=False
                        break
                    checked=False
                    for x in range (len(myMap)):
                        try:
                            if(checked==False):
                                if (myMap[i-x-1][pColumn]!="□"):
                                    checked=True
                                    if(i-x-1<0):
                                        checked=False
                                        break
                        except IndexError:
                            break
                    if (checked==False):
                        myMap[i-1][pColumn]=myMap[i][pColumn]
                        myMap[i][pColumn]=" "
                    else:
                        for k in range(len(myMap)):
                            if (myMap[i-k-1][pColumn]!="□"):
                                break
                        if(myMap[i-k-1][pColumn]=="█"):
                            print("There is something blocking your path!\nChoose something else.")
                            works=False
                            break
                        for j in range (k+1,0,-1):
                            myMap[i-j][pColumn]=myMap[i-j+1][pColumn]
                        myMap[i][pColumn]=" "
                if(pInput=="S"):
                    if(i==(len(myMap)-1)):
                        print("Don't throw yourself off the edge now.")
                        works=False
                        break
                    checked=False
                    for x in range (len(myMap)):
                        try:
                            if(checked==False):
                                if (myMap[i+x+1][pColumn]!="□"):
                                    checked=True
                                    if(i+x+1>len(myMap)):
                                        checked=False
                                        break
                        except IndexError:
                            break
                    if (checked==False):
                        myMap[i+1][pColumn]=myMap[i][pColumn]
                        myMap[i][pColumn]=" "
                    else:
                        for k in range(len(myMap)):
                            if (myMap[i+k+1][pColumn]!="□"):
                                break
                        if(myMap[i+k+1][pColumn]=="█"):
                            print("There is something blocking your path!\nChoose something else.")
                            works=False
                            break
                        for j in range (k+1,0,-1):
                            myMap[i+j][pColumn]=myMap[i+j-1][pColumn]
                        myMap[i][pColumn]=" "
                if(pInput=="A"):
                    if(pColumn==0):
                        print("Don't throw yourself off the edge now.")
                        works=False
                        break
                    checked=False
                    for x in range (len(myMap[0])):
                        try:
                            if(checked==False):
                                if (myMap[i][pColumn-x-1]!="□"):
                                    checked=True
                                    if(pColumn-x-1<0):
                                        checked=False
                                        break
                        except:
                            break
                    if (checked==False):
                        myMap[i][pColumn-1]=myMap[i][pColumn]
                        myMap[i][pColumn]=" "
                    else:
                        for k in range(len(myMap[0])):
                            if (myMap[i][pColumn-k-1]!="□"):
                                break
                        if(myMap[i][pColumn-k-1]=="█"):
                            print("There is something blocking your path!\nChoose something else.")
                            works=False
                            break
                        for j in range (k+1,0,-1):
                            myMap[i][pColumn-j]=myMap[i][pColumn-j+1]
                        myMap[i][pColumn]=" "
                if(pInput=="D"):
                    if(pColumn==(len(myMap[i])-1)):
                        print("Don't throw yourself off the edge now.")
                        works=False
                        break
                    checked=False
                    for x in range (len(myMap[0])):
                        try:
                            if(checked==False):
                                if (myMap[i][pColumn+x+1]!="□"):
                                    checked=True
                                    if(pColumn+x+1>len(myMap[i])):
                                        checked=False
                                        break
                        except IndexError:
                            break
                    if (checked==False):
                        myMap[i][pColumn+1]=myMap[i][pColumn]
                        myMap[i][pColumn]=" "
                    else:
                        for k in range(len(myMap[0])):
                            if (myMap[i][pColumn+k+1]!="□"):
                                break
                        if(myMap[i][pColumn+k+1]=="█"):
                            print("There is something blocking your path!\nChoose something else.")
                            works=False
                            break
                        for j in range (k+1,0,-1):
                            myMap[i][pColumn+j]=myMap[i][pColumn+j-1]
                        myMap[i][pColumn]=" "
        for i in range (len(checkMap)):
            for k in range (len(checkMap[i])):
                if(checkMap[i][k]==("◯"or"⧇"or"⟐")):
                    if(myMap[i][k]=="□"):
                        myMap[i][k]="⧇"
                    elif(myMap[i][k]=="◆"):
                        myMap[i][k]="⟐"
                    else:
                        myMap[i][k]="◯"
        printMap(myMap)
        checked=False
        for i in range(len(myMap)):
            for k in range(len(myMap[i])):
                if(myMap[i][k]=="⟐" or myMap[i][k]=="◯"):
                    checked=True
                if(checked==False and i+1==len(myMap) and k+1==len(myMap[i])):
                    checked=True
                    win=True
                    print("\nYou won the game!\n")
    while (True):
        redo=input("Would you like to play another game? Yes or no? ").upper()
        if (redo=="YES"):
            redo=True
            break
        elif(redo=="NO"):
            redo=False
            break
        else:
            print("Just type yes or no please, no extra things.")
