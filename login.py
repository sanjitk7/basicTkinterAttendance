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
    # print(dbPass)
    if (password.get()==dbPass[0]):
        print("LOGIN SUCCESSFUL!")
        loginFrame.pack_forget()
    else:
        print("INVALID LOGIN!")

    return

#window
tkWindow1 = tk.Tk()
loginFrame = tk.Frame(tkWindow1)
tkWindow1.geometry('400x150')  
tkWindow1.title('Login To Attendance Manager')

#username label and text entry box
usernameLabel = tk.Label(loginFrame, text="User Name")
usernameLabel.grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(loginFrame, textvariable=username)
usernameEntry.grid(row=0, column=1)

#password label and password entry box
passwordLabel = tk.Label(loginFrame,text="Password")
passwordLabel.grid(row=1, column=0)  
password = tk.StringVar()
passwordEntry = tk.Entry(loginFrame, textvariable=password, show='*')
passwordEntry.grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(loginFrame, text="Login", command=validateLogin)
loginButton.grid(row=4, column=0)  

loginFrame.pack()
tkWindow1.mainloop()