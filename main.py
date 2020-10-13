from openTicket import *

input = input("Please describe your issue: ")

t1 = Ticket(input, "open")
t1.displayIssue()
print("State is:", t1.getState())

t2 = Ticket("No more issues", "closed")
t2.displayIssue()
print("State is:", t2.getState())
t2.setState("open")
print("State changed to:", t2.getState())

t1.displayIssue()

t1.startTime()
