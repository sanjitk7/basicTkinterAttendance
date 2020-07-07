import tkinter as tk
from functools import partial
from db import mycursor


def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    # query = "select * from t_users where full_name=%s" % username.get()
    # print(query)
    mycursor.execute("select pass from t_users where full_name=%s",(username.get(),))
    dbPass = mycursor.fetchone()
    print(dbPass)
    if (password.get()==dbPass[0]):
        print("Redirect to Dashboard")

    return

#window
tkWindow = tk.Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Login To Attendance Manager')

#username label and text entry box
usernameLabel = tk.Label(tkWindow, text="User Name")
usernameLabel.grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(tkWindow, textvariable=username)
usernameEntry.grid(row=0, column=1)

#password label and password entry box
passwordLabel = tk.Label(tkWindow,text="Password")
passwordLabel.grid(row=1, column=0)  
password = tk.StringVar()
passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*')
passwordEntry.grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin)
loginButton.grid(row=4, column=0)  


tkWindow.mainloop()