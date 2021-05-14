from Subject import Subject
from tkinter import *

import pickle

class User:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

        self.d = {}


        next_row = 0



    def add_subject(self, name):
        d = {name: Subject(name)}
        self.subjects.update(d)

    def start_session(self, name):
        subject = self.subjects[name]
        subject.start_session()

    def stop_session(self, name):
        subject = self.subjects[name]
        subject.finish_session()

    def user_window(self):

        root = Tk()
        root.geometry("1000x1000")

        def root_on_closing():
            f = open("Usrs/" + self.name + ".bin", "wb")
            pickle.dump(self, f)
            f.close()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", root_on_closing)

        label = Label(root, text="hello " + self.name)
        label.grid()

        def add_entry_fct():
            self.add_subject(add_entry.get())
            add_entry.delete(0, 'end')

        add_button = Button(root, text="Add subject", command=add_entry_fct)
        add_button.grid()



        add_entry = Entry(root)
        add_entry.grid()




        for key in self.subjects:
            subject = self.subjects[key]

            def session_button_fct():
                subject.session_button_fct(session_button)
            session_button=\
                Button(root, bg ="#EE6041", text = subject.name, height = 10, width =20, command=session_button_fct)

            session_button.grid()

            def time_button_fct():
                subject.time_button_fct(time_button)


            time_button = \
                Button(root, bg="white", text="time", height=10, width=20, command=time_button_fct)

            time_button.grid()




        root.mainloop()



