from time import strftime
from time import gmtime
from time import time

from tkinter import *
from tkinter import Tk, mainloop, TOP

from Session import Session
#represents a subject

class Subject:
    def __init__(self, name):
        self.name = name
        self.sessions =[]
        self.cummulated_time=0
        self.active_session = None #represents the active session for a subject and is None to show there is no Session running

    def number_of_sessions(self):
        return len(self.sessions)

    def cummulated_time_formatted(self):
        return strftime("%H:%M:%S", gmtime(self.cummulated_time))

    def start_session(self):
        if self.active_session == None:
            self.active_session = Session(self)
            self.active_session.start()
            self.sessions.append(self.active_session)
        else:
            print("This subject already runs a time")

    def stop_session(self):
        if self.active_session != None:
           self.active_session.stop()
           self.cummulated_time += self.active_session.needed_time
           self.active_session = None
        else:
            print("This subject isn't running a session which could be stopped")

    def session_button_fct(self, session_button):
        if self.active_session == None:
            self.start_session()
            session_button.config(bg="#5DC87C")
        else:
            self.stop_session()
            session_button.config(bg="#EE6041")

    def time_button_fct(self, time_button):
        time_button.config(text=self.cummulated_time_formatted())








