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
    tickets = []
    while finished == 0:
        count = getLastId()
        print("\n" * 100)
        print("Hoot Ticket Management\n")
        print("Please select from one of the choices below")
        print("""
                            1. Open a new ticket.
                            2. Add comments to a ticket.
                            3. Show all open tickets.
                            4. View a ticket.
                            0. Exit
                            
                            Number of tickets open: """, count, """
Selection: """)
        selection = input()

        # Open a new ticket
        if selection == "1":
            a = 0
            while a == 0:
                print("Please describe the request or incident")
                n = input()
                print("Successfully logged ticket request\n")
                addTicket(n)
                id = getLastId()
                print("Ticket ID:", id)
                print("\nWould you like to open another ticket? (y/n)")
                n = input()
                if n == "n" or n == "N" or n == "no" or n == "NO":
                    a = 1

        # Add comments to a ticket
        elif selection == "2":
            print("Would you like to view all tickets to get ID? (y/n)")
            n = input()
            # Display all open tickets so user can get ID #
            if n == "y" or n == "Y" or n == "yes" or n == "YES":
                showAll()

            print("Please enter ticket ID")
            id = input()
            print("You have selected: " + n)
            print("Comment to add?")
            comment = input()
            addComment(id, comment)
            print("Enter any key to return to the menu.")
            n = input()




        # Display all open tickets
        elif selection == "3":
            showAll()
            print("Enter any key to return to the menu.")
            n = input()

        # View a ticket
        elif selection == "4":
            print("Would you like to view all tickets to get ID? (y/n)")
            n = input()
            # Display all open tickets so user can get ID #
            if n == "y" or n == "Y" or n == "yes" or n == "YES":
                showAll()

            print("Please enter ticket ID")
            n = input()
            viewTicket(n)

            print("Enter any key to return to the menu.")
            n = input()


        # Exit program
        elif selection == "0":
            finished = 1
            sys.exit


