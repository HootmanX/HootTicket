import time

class Ticket:
        def __init__(self, issue, status):
            self.issue = issue
            self.startTime = time.localtime() # potential issue with timezones

        def displayIssue(self):
            print(self.issue)
        
        def state(self, status):
                self.status=status
