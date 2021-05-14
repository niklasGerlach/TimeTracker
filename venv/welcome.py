#represents the welcome window to log in
from tkinter import *
from user import User

import pickle
import os.path


root = Tk()
root.geometry("1000x1000")

welcome_label = Label(root, text = "Welcome! Pls enter your name to log in")
welcome_label.grid(row = 0)

entry_name = Entry(root)
entry_name.grid(row =1)

def enter_name_fct():
    name = entry_name.get()
    if name == "":
        welcome_label.config(text = "Pls enter a name before submitting")

    elif os.path.isfile("Usrs/" + name + ".bin"):
       file = open("Usrs/" + name + ".bin", "rb")
       user = pickle.load(file)
       root.destroy()
       user.user_window()




    else:
        user = User(name)
        f = open("Usrs/" + name + ".bin", "wb")
        pickle.dump(user, f)
        f.close()





enter_name = Button(root, text = "submit", command = enter_name_fct)
enter_name.grid(row=2)




root.mainloop()

print()
