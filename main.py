from openTicket import *
import time
import sys

def main():
    login()
 
def login():
    username="root"
    password="hoot"
    print("Enter username: ")
    inputUser=input()
    print("Enter password: ")
    inputPass=input()
    
    if username == inputUser and password == inputPass:
        print("Access Granted!")
        menu()
    else :
        print("Access Denied - Incorrect Username and/or Password")
        login()
        
def menu():
    tickets = []
    holder = {issue: Ticket(issue=issue) for issue in tickets} # work on this
    #num = [] unused at the moment
    print("Please select from on of the choices below")
    #time.sleep(1)
    selection = input("""
                        1. Open a new ticket.
                        2. Add comments to a ticket
                        3. Close a ticket
                        0. Exit
                        
                        Selection: """)
                        
                        
    if selection == "1" :
        print("Please describe the request or incident")
        issue=input()
        tickets.append(issue)
        holder[].displayIssue()
        
    elif choice == "0" :
        sys.exit


main()
