import time
import os
from tkinter import *
from tkinter import Tk, mainloop, TOP
from Subject import Subject



class subject_view:
    next_row = 0

    def __init__(self, subject_name):
        self.subject = Subject(subject_name)

        #create and place button for starting session
        self.session_button =\
            Button(root, bg ="#EE6041", text = self.subject.name, height = 10, width =20, command=self.session_button_fct)

        self.session_button.grid(row=subject_view.next_row, column =0)

        subject_view.next_row += 1


        #create field for showing time
        self.time_button =\
            Button(root, bg = "white", text = "time",  height = 10, width =20, command = self.time_button_fct )

        self.time_button.grid(row = self.next_row-1, column =1)


    def time_button_fct(self):
        self.time_button.config(text = self.subject.cummulated_time_formatted())


    def session_button_fct(self):
        if self.subject.active_session ==None:
            self.subject.start_session()
            self.session_button.config(bg ="#5DC87C")
        else:
            self.subject.stop_session()
            self.session_button.config(bg="#EE6041")

###end of class subject view



root = Tk()
root.geometry("1000x1000")

subject_view("math")
subject_view("aud")

#entry field and button for adding a new subject
new_subject_entry = Entry(root)
new_subject_entry.grid()

def new_subject_button_fct():
    subject_view(new_subject_entry.get())


new_subject_button = Button(root, text="add subject", command =new_subject_button_fct)
new_subject_button.grid()




root.mainloop()







