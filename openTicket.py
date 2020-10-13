import time

class Ticket:
        def __init__(self, issue):
            self.issue = issue
            self.startTime = time.localtime() # potential issue with timezones

        def displayIssue(self):
            print(self.issue)
