database={}

def addtask(database):
    name=input("Enter the name : ")
    id1=input("Enter the ID : ")
    status=input("Enter the status : ")
    database[id1]=[name,status]
    print("Task added")

def updatetask(database):
    id1=input("Enter the ID : ")
    d1=database.keys()
    for i in d1:
        if(i != id1):
            print("id not found")
            return 0
            
    c=input("Whether to change name or status : ")
    if (c.lower() in "name"):
        name=input("Enter the name : ")
        database[id1][0]=name

    elif (c.lower() in "status"):
        status=input("Enter the status : ")
        database[id1][1]=status

    else:
        print("Invalid input")

def deletetask(database):
    name=input("Enter the name : ")
    d2=database.keys()
    for i in d2:
        if(database[i][0] not in name):
            print("task not found")
            return 0
        else:
            database.pop(i)
            print("Task deleted ")

def listtask(database):
    d1=database.keys()
    print("ID\tNAME\tSTATUS")
    for i in d1:
        print(i,database[i][0],database[i][1])
        
def searchtask(database):            
    c=input("Whether to search using name or id : ")
    if (c.lower() in "name"):
        name=input("Enter the name : ")
        d2=database.keys()
        for i in d2:
            if(database[i][0] not in name):
                print("task not found")
                return 0
            else:
                print(i,database[i])

    elif (c.lower() in "status"):
        status=input("Enter the status : ")
        d2=database.keys()
        for i in d2:
            if(database[i][1] not in status):
                print("task not found")
                return 0
            else:
                print(i,database[i])

    else:
        print("Invalid input")

def listtaskbyname(database):            
    c=input("Enter the letter ")
    d2=database.keys()
    for i in d2:
        if(database[i][0][-1] not in c):
            print("task not found")
            return 0
        else:
            print(i,database[i])
        

c=0

while(0<=c<=7):
    print("1.Add task")
    print("2.Upadate information")
    print("3.Delete task")
    print("4.List the tasks")
    print("5.Search the task")
    print("6.List task by last letter ")
    print("7.EXIT")
    c=int(input("Enter your choice : "))

    if(c==1):
        addtask(database)
        print()
    elif(c==2):
        updatetask(database)
        print()
    elif(c==3):
        deletetask(database)
        print()
    elif(c==4):
        listtask(database)
        print()
    elif(c==5):
        searchtask(database)
        print()
    elif(c==6):
        listtaskbyname(database)
        print()
    else:
        break
else:
    print("Wrong input")

