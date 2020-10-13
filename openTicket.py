from datetime import datetime

class Ticket:
        def __init__(self, issue, state):
            self.issue = issue
            self.state = state
            # Grab time as start of ticket
            self.now = datetime.now()
            self.openTime = self.now.strftime("%m/%d/%Y, %H:%M:%S")
            self.notes = []

        def displayIssue(self):
            print(self.issue)
        
        def setState(self, state):
                self.state=state

        def getState(self) :
            return self.state
            
        def startTime(self) :
            print(self.openTime)
            
        def addNotes(self, comment) :
            self.notes.append(comment)
            
        def displayNotes(self) :
            print (list(enumerate(self.notes)))
