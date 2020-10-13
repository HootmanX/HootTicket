from openTicket import *
import sys



def login():
    # Password needs restructuring to call from hashed password files
    username = "root"
    password = "hoot"
    print("Hoot Ticket Management\n")
    print("Enter username: ")
    inputUser = input()
    print("Enter password: ")
    inputPass = input()

    if username == inputUser and password == inputPass:
        print("Access Granted!")
        menu()
    else:
        print("Access Denied - Incorrect Username and/or Password")
        login()


def menu():
    finished = 0
    ticketID = 0  # problematic on reopening console (possible save data to file/database?)
    tickets = []
    while finished == 0:
        print("\n" * 100)
        print("Hoot Ticket Management\n")
        print("Please select from one of the choices below")
        selection = input("""
                            1. Open a new ticket.
                            2. Add comments to a ticket.
                            3. Show all open tickets.
                            4. Close a ticket.
                            0. Exit
                            
                            Number of tickets open: """ + str(ticketID) + """
                            Selection: """)

        # Open a new ticket
        if selection == "1":
            a = 0
            while a == 0:
                print("Please describe the request or incident")
                n = input()
                tickets.append(Ticket(ticketID, n))
                print("Logged ticket request: ")
                tickets[ticketID].displayIssue()
                ticketID += 1
                print("Would you like to open another ticket? (y/n)")
                n = input()
                if n == "n" or n == "N" or n == "no" or n == "NO":
                    a = 1

        # Add comments to a ticket
        elif selection == "2":
            print("Would you like to view all tickets to get ID? (y/n)")
            n = input()
            # Display all open tickets so user can get ID #
            if n == "y" or n == "Y" or n == "yes" or n == "YES":
                a = 0
                for i in tickets:
                    a += 1
                    print("Ticket #" + str(a) + ":" + i.issue)
                    print("\n\n")
            print("Please enter ticket ID")
            n = input()
            m = int(n)
            print("You have selected: " + n)
            print("Comment to add?")
            com = input()
            tickets[m].addNotes(com)
            print("Displaying all comments on ticket")
            tickets[m].displayNotes()
            print("Enter any key to return to the menu.")
            n = input()




        # Display all open tickets
        elif selection == "3":
            a = 0
            for i in tickets:
                a += 1
                print("Ticket #" + str(a) + ":" + i.issue)
                print("Ticket was opened on ")
                i.showTime()
                print("\n")

            print("Enter any key to return to the menu.")
            n = input()


        # Exit program
        elif selection == "0":
            finished = 1
            sys.exit
