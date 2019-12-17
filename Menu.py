#Functions
import sys

def mainMenu(): #Opens menu
    print("1) Can a person check out a certain book?")
    print("2) Can a person return a certain book?")
    print("3) What is the list of people with late fees and how much?")
    print("4) What is the usage of each book? Which are the top used books?")
    print("5) Press 5 to exit the program")
    return

def first(): #First request
    print("Check this out.")
    print("1) Return to menu")
    return

def second(): #Second Request
    print("Return this one.")
    print("1) Return to menu")
    return

def third(): #Third Request
    print("List of people.")
    print("1) Return to menu")
    return

def fourth(): #Fourth Request
    print("Usage of each book.")
    print("1) Return to menu")
    return

def fifth(): #Closes the program entirely
    print("FinalProject.exe has stopped working")
    sys.exit()
    return

def loopMain(choice): #Directs to the proper request
    if choice == 1:
        first()
    elif choice == 2:
        second()
    elif choice == 3:
        third()
    elif choice == 4:
        fourth()
    elif choice == 5:
        fifth()
    else:
        print("Come on bro")

def loopOptions(choice): #A way back to menu
    if choice == 1:
       mainMenu()
       choice = int(input(""))
       loopMain(choice)
       choice = int(input(""))
       loopOptions(choice)

def reader():
    fread = open("booklist.txt", "r")
    for line in fread:
        line = line.rstrip("\n")
        numCopy.append(line.find("#"))
    fread.close()
    print("DONE")
    return


        

#Main body of code
i = 0
numCopy = [] #index one spot before number of copies

       
mainMenu()
choice = int(input(""))
loopMain(choice)
reader()

print(numCopy)

choice = int(input(""))
loopOptions(choice)





#Read/Write



