from queue import Empty

choice = str(input("Would you like to see your tasks 'S', add a task 'A', or check off a task? 'C' "))
choice = choice.upper()



listoftasks = []
number = 0
numlist = []


def returnMenu():
    choice = input("\nWould you like to see your tasks 'S', add a task 'A', or check off a task? 'C' ")
    choice = choice.upper()
    if choice == 'S':
        if not listoftasks:
            print("\nNo tasks added yet!")
            showTasks()
        else:
            print("")
            showTasks()

    if choice == 'A':
        addTask()
    
    if choice == 'C':
        completeTask()
    else:
        print("\nInvalid input, please try again.")
        returnMenu()

def showTasks():
    for (i,item) in enumerate(listoftasks, start=1):
        print(str(i) + '.', item)
    returnMenu()

def addTask():
    print("")
    add = input("Add a task: ")
    listoftasks.append(add)
    print("")
    showTasks()
    returnMenu()

def completeTask():
    while True:
        if not listoftasks:
            print("\nYou don't have any tasks to complete!")
            returnMenu()
            break
        else:
            print("")
            for (i,item) in enumerate(listoftasks, start=1):
                print(str(i) + '.', item)
            try:
                delete = int(input("\nWhich task have you completed? "))
                listoftasks.pop((delete-1))
                print("")
            except:
                print("\nInvalid input, please try again.\n")
            if not listoftasks:
                print("\nYou've completed all of your tasks!")
            else:
                for (i,item) in enumerate(listoftasks, start=1):
                    print(str(i) + '.', item)
            returnMenu()

if choice == 'S':
    if not listoftasks:
        print("\nNo tasks added yet!")
        returnMenu()
    showTasks()
if choice == 'A':
    addTask()
if choice == 'C':
    if not listoftasks:
        print("\nYou don't have any tasks to complete!")
        returnMenu()
    else:
        completeTask()
else:
    print("\nInvalid input, please try again.")
    returnMenu()













