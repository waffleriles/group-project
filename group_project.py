def menu():
    print("\nFellowship of the Ring Developed by <Carmen Brewers> on <03/21/2024>")
    print("======================================================++++==")
    print("\tA. Add Client.")
    print("\tB. Book Event.")
    print("\tC. Print Company.") 
    print("\tD. Print Client.")
    print("\tE. Cancel Booking")
    print("\tX. Exit") 
    option = input("Option: ").upper()
    option = option[0] # I'll take just the first character
    return option

#checks if an id is already used for a client
#returns true if the client is in the dictionary
#returns false if the client is not in the dictionary
def checkID(id):
    for key in company.keys():
        if key == id:
            return True
    return False

def addClient(company, id, name):
#adds a client to the dictionary if they do not already exist
#uses input from user for client id and name
    for key in company.keys():
        if checkID(id):
            print("Client ID: ", id)
            print("Client Name: ", company["id"]["name"])
            print("ID previously stored. Operation ignored.")
        return ""
    company[id] = {"ID: ": str(id), "Name: ": str(name)}
    return ""

def bookEvent(company, id):
    for key in company.keys():
        if not checkID:
            print("That ID doesn't exist. Try again.")
        
        date = input("What time is your event? ")
        company[id] = {"Date: ": str(date)}
        place = input("Where is your event located? ")
        company[id] = {"Place: ": str(place)}
        placeCost = input("How much will the place cost? ")
        company[id] = {"Place Cost: ": str(placeCost)}
        employeeCost = input ("How much is the employee cost? ")
        company[id] = {"Employee Cost: ": str(employeeCost)}


def printCompany(company, id):
    for client in company:
        printClient(company, id)

def printClient(company, id):
    if not checkID:
        print("Client is not in system")
    
    print("Client", company[id]["Name: "])
    print("Events: ")
    print("Date: ", company[id]["Name: "])
    print("Place: ", company[id]["Place: "])
    print("Employee Cost: ", company[id]["Employee Cost"])

    return ""

def cancelBooking(company, id):

    if not checkID:
        print("Client is not in system")

    

def printCompany(id):
    date = input("Date to Cancel")
    for event in company:
        if event == date:
            print("Event on ", date, "has been canceled.")
        else:
            print("Event on", date, "was not found for this client.")
        
        return ""

#Main Program
company = {}
op = ""
while op!="X":
    op = menu()
    if op=="A":
        id = input("Client ID: ")
        name = input("Client Name: ")
        addClient(company, id, name)
    elif op=="B":
        id = input("Client ID: ")
        bookEvent(company, id)
    elif op=="C":
        printCompany(id)
    elif op=="D":
        id = input("Client ID: ")
        printClient(company, id)
    elif op=="E":
        id = input("Client ID: ")
        cancelBooking(company, id)
    elif op=="X":
        print("Good Bye ...Have a good day!!")
    else:
        print("Wrong option ...")