import time
import calendar
#represents on session for a given subject

class Session:

    def __init__(self, subject):
        self.subject = subject
        self.running = False
        self.finished = False
        self.starting_time =""
        self.finishing_time =""
        self.needed_time=""


    def start(self):
        if self.running:
            print("Session is already running")
        else:
            self.running =True
            self.starting_time = time.localtime()





    def stop(self):
        if self.running:
            self.finished = True
            self.running = False
            self.finishing_time = time.localtime()
            self.needed_time = time.mktime(self.finishing_time) - time.mktime(self.starting_time)





            
        else:
            print("Session is not running")











    
    
    
    